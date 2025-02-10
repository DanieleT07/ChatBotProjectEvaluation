import torch
import ollama
import os
from openai import OpenAI
import argparse
import json
import re
import yaml

# ANSI escape codes for colors
PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

config_path = "config.yaml"
config = yaml.safe_load(open(config_path, 'r'))

# Loading of variables from the config file
top_k_var = config['top_k']
system_message = config['system_message']
embeding_model = config['ollama_model_emebeding']
embeddings_path = config['embeddings_file']
ollama_api = config['ollama_api_base_url']
vault_path = config['vault_file']
vault_old_path = config['vault_old_file']
ollama_model = config['ollama_model']
ollama_api_key = config['ollama_api_key']

# Function to open a file and return its contents as a string
def open_file(filepath):
    """
    Opens the given file and returns its contents as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def find_matching_lines(file_path, input_string):
    # Find all occurrences of the patterns in the input string
    matches = re.findall(r'\b(?:A?\d{3}|a\d{3})\b', input_string)
    
    # Extract only the numeric part from the matches
    codes = {int(m[-3:]) for m in matches}  # Extracts the last 3 digits as integers

    line_numbers = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            found = False
            
            # Check for direct matches like Axxx
            if any(re.search(rf'\bA{code}\b', line) for code in codes):
                line_numbers.append(i)
                found = True  # Flag to continue checking other matches
            
            # Check for range matches like Axxx/yyy
            ranges = re.findall(r'A(\d{3})/(\d{3})', line)
            for start, end in ranges:
                if any(int(start) <= code <= int(end) for code in codes):
                    line_numbers.append(i)
                    found = True  # Flag to continue checking other matches
            
            if found:
                continue  # Continue to the next line to find all matches

    return sorted(set(line_numbers))  # Remove duplicates and sort

def get_lines_from_file(line_numbers, file_path):
    # Given a list of line numbers and a file path, return the corresponding lines from the file.
    # :param line_numbers: List of integers representing line numbers (1-based index)
    # :param file_path: Path to the file
    # :return: List of strings containing the corresponding lines
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        return [lines[i - 1].rstrip('\n') for i in line_numbers if 1 <= i <= len(lines)]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Function to get relevant context from the vault based on user input
def get_relevant_context(rewritten_input, vault_embeddings, vault_content, top_k=top_k_var):
    # Given a rewritten user query, the vault embeddings, and the vault content,
    # returns the top-k relevant context from the vault.
    control = False
    line_numbers = find_matching_lines(vault_path, rewritten_input)
    if line_numbers != []:
        control = True
        relevant_context_strict = get_lines_from_file(line_numbers, vault_path)
        rewritten_input = rewritten_input.join(relevant_context_strict)
    else:
        relevant_context_strict = []
    if vault_embeddings.nelement() == 0:  # Check if the tensor has any elements
        return []
    # Encode the rewritten input
    input_embedding = ollama.embeddings(model=embeding_model, prompt=rewritten_input)["embedding"]
    # Compute cosine similarity between the input and vault embeddings
    cos_scores = torch.cosine_similarity(torch.tensor(input_embedding).unsqueeze(0), vault_embeddings)
    # Adjust top_k if it's greater than the number of available scores
    print("Cosine Similarity Scores:", cos_scores)
    print("Vault Embeddings:", vault_embeddings)
    top_k = min(top_k, len(cos_scores))
    # Sort the scores and get the top-k indices
    top_indices = torch.topk(cos_scores, k=top_k)[1].tolist()
    # Get the corresponding context from the vault
    relevant_context_loose = [vault_content[idx].strip() for idx in top_indices]
    relevant_context = [*relevant_context_strict, *relevant_context_loose]
    return relevant_context

def rewrite_query(user_input_json, conversation_history, ollama_model):
    # Rewrites the given user query based on the conversation history.
    user_input = json.loads(user_input_json)["Query"]
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history[-2:]])
    prompt = f"""Rewrite the following query by incorporating relevant context from the conversation history, but only if the new query is related to the history.
    The rewritten query should:
    
    - Preserve the core intent and meaning of the original query
    - Expand and clarify the query to make it more specific and informative for retrieving relevant context
    - Avoid introducing new topics or queries that deviate from the original query
    - DONT EVER ANSWER the Original query, but instead focus on rephrasing and expanding it into a new query
    
    Return ONLY the rewritten query text, without any additional formatting or explanations.
    
    Conversation History (exclude the following message if it doesn't provide relevant information for the new query):
    {context}
    
    Original query: [{user_input}]
    
    Rewritten query: 
    """
    response = client.chat.completions.create(
        model=ollama_model,
        messages=[{"role": "system", "content": prompt}],
        max_tokens=200,
        n=1,
        temperature=0.1,
    )
    rewritten_query = response.choices[0].message.content.strip()
    return json.dumps({"Rewritten Query": rewritten_query})
   
def ollama_chat(user_input, system_message, vault_embeddings, vault_content, ollama_model, conversation_history):
    # Handles the core logic of the Ollama chat.
    # Add the user's input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # If the conversation history has more than one item, rewrite the query
    if len(conversation_history) > 1:
        # Create a JSON object with the query and the rewritten query
        query_json = {
            "Query": user_input,
            "Rewritten Query": ""
        }
        # Rewrite the query
        rewritten_query_json = rewrite_query(json.dumps(query_json), conversation_history, ollama_model)
        # Parse the rewritten query JSON
        rewritten_query_data = json.loads(rewritten_query_json)
        # Get the rewritten query
        rewritten_query = rewritten_query_data["Rewritten Query"]
        # Print the original query and the rewritten query
        print(PINK + "Original Query: " + user_input + RESET_COLOR)
        print(PINK + "Rewritten Query: " + rewritten_query + RESET_COLOR)
    else:
        # If the conversation history has only one item, use the original query
        rewritten_query = user_input
    
    # Get the relevant context from the vault based on the rewritten query
    relevant_context = get_relevant_context(rewritten_query, vault_embeddings, vault_content)
    # If relevant context is found, print it
    if relevant_context:
        context_str = "\n".join(relevant_context)
        print("Context Pulled from Documents: \n\n" + CYAN + context_str + RESET_COLOR)
    else:
        print(CYAN + "No relevant context found." + RESET_COLOR)
    
    # Add the relevant context to the user's input
    user_input_with_context = user_input
    if relevant_context:
        user_input_with_context = user_input + "\n\nRelevant Context:\n" + context_str
    
    # Update the conversation history with the user's input with context
    conversation_history[-1]["content"] = user_input_with_context
    
    # Create a message history for the Ollama model
    messages = [
        {"role": "system", "content": system_message},
        *conversation_history
    ]

    print(messages)
    
    # Send the completion request to the Ollama model
    response = client.chat.completions.create(
        model=ollama_model,
        messages=messages,
        max_tokens=2000,
    )
    
    # Add the Ollama model's response to the conversation history
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    
    # Return the Ollama model's response
    return response.choices[0].message.content


def check_different_embeddings(vault_old_path, vault_path):
    with open(vault_old_path, "r", encoding='utf-8') as f:
        old_content = f.read()
    with open(vault_path, "r", encoding='utf-8') as f:
        new_content = f.read()
    return old_content != new_content

def save_old_embeddings(embeddings_path, embeddings):
    with open(embeddings_path, "w", encoding='utf-8') as f:
        json.dump(embeddings, f)

def load_old_embeddings(embeddings_path):
    with open(embeddings_path, "r", encoding='utf-8') as f:
        return json.load(f)

def save_old_vault(vault_path, vault_content):
    with open(vault_old_path, "w", encoding='utf-8') as f:
        #clean the file
        f.write("")
    with open(vault_old_path, "a", encoding='utf-8') as f:
        for line in vault_content:
            f.write(line)


# Parse command-line arguments
print(NEON_GREEN + "Parsing command-line arguments..." + RESET_COLOR)
parser = argparse.ArgumentParser(description="Ollama Chat")
parser.add_argument("--model", default=ollama_model, help="Ollama model to use (default: llama3)")
args = parser.parse_args()

# Configuration for the Ollama API client
print(NEON_GREEN + "Initializing Ollama API client..." + RESET_COLOR)
client = OpenAI(
    base_url=ollama_api,
    api_key=ollama_api_key
)

# Load the vault content
print(NEON_GREEN + "Loading vault content..." + RESET_COLOR)
vault_content = []
if os.path.exists(vault_path):
    with open(vault_path, "r", encoding='utf-8') as vault_file:
        vault_content = vault_file.readlines()

# Generate embeddings for the vault content using Ollama
print(NEON_GREEN + "Generating embeddings for the vault content..." + RESET_COLOR)
vault_embeddings = []

if check_different_embeddings(vault_old_path, vault_path):
    for content in vault_content:
        response = ollama.embeddings(model=embeding_model, prompt=content)
        vault_embeddings.append(response["embedding"])
else:
    vault_embeddings = load_old_embeddings(embeddings_path)



# Convert to tensor and print embeddings
print("Converting embeddings to tensor...")
vault_embeddings_tensor = torch.tensor(vault_embeddings) 
print("Embeddings for each line in the vault:")
print(vault_embeddings_tensor)

# Conversation loop
print("Starting conversation loop...")
conversation_history = []

while True:
    user_input = input(YELLOW + "Ask a query about your documents (or type 'quit' to exit): " + RESET_COLOR)
    if user_input.lower() == 'quit':
        save_old_embeddings(embeddings_path, vault_embeddings)
        save_old_vault(vault_path, vault_content)
        break
    
    response = ollama_chat(user_input, system_message, vault_embeddings_tensor, vault_content, args.model, conversation_history)
    print(NEON_GREEN + "Response: \n\n" + response + RESET_COLOR)


