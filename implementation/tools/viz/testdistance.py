import torch
import torch.nn.functional as F
import ollama
import logging
import random

# Setup logging to a file
#logging.basicConfig(filename="cosine_similarity.log", level=logging.DEBUG, format='%(asctime)s - %(message)s')

def cosine_similarity_score(str1, str2, log_file="cosine_similarity.log"):
    """
    Computes the cosine similarity between two string embeddings using a real embedding model
    and logs details to a file.
    """
    # Get embeddings for both strings using Ollama
    embedding1 = ollama.embeddings(model='mxbai-embed-large', prompt=str1)["embedding"]
    embedding2 = ollama.embeddings(model='mxbai-embed-large', prompt=str2)["embedding"]

    # Convert embeddings to tensors
    embedding1_tensor = torch.tensor(embedding1, dtype=torch.float32)
    embedding2_tensor = torch.tensor(embedding2, dtype=torch.float32)

    # Normalize the vectors
    norm_embedding1 = F.normalize(embedding1_tensor.unsqueeze(0), p=2, dim=1)
    norm_embedding2 = F.normalize(embedding2_tensor.unsqueeze(0), p=2, dim=1)

    # Compute cosine similarity
    similarity = F.cosine_similarity(norm_embedding1, norm_embedding2).item()

    # Log embeddings and debug info
    with open(log_file, "a") as log:
        log.write(f"String 1: {str1}\n")
        log.write(f"String 2: {str2}\n")
        #log.write(f"Raw Embedding 1: {embedding1}\n")
        #log.write(f"Raw Embedding 2: {embedding2}\n")
        #log.write(f"Normalized Embedding 1: {norm_embedding1.tolist()}\n")
        #log.write(f"Normalized Embedding 2: {norm_embedding2.tolist()}\n")
        log.write(f"Cosine Similarity Score: {similarity}\n")
        log.write("="*50 + "\n")

    return similarity


# Example usage

str1 = "Music"
str2 = "Harmony"
score = cosine_similarity_score(str1, str2)
print("Cosine Similarity Score:", score)

arrayOfSentences = [
    "Good morning, everyone!", 
    "The sun is shining brightly today.", 
    "She enjoys reading historical novels.", 
    "Learning a new language takes time and effort.", 
    "A cup of coffee can be very refreshing.", 
    "They decided to take a road trip across the country.", 
    "The dog barked excitedly when it saw its owner.", 
    "Cooking at home is often healthier than eating out.", 
    "The internet has changed the way we communicate.", 
    "Music has the power to bring people together.",
    "He finished his work before the deadline.", 
    "A balanced diet is important for good health.", 
    "They watched the sunset from the top of the hill.", 
    "The library is a great place to study quietly.", 
    "She wrote a heartfelt letter to her friend.", 
    "Exercising regularly improves overall well-being.", 
    "The artist spent hours perfecting his painting.", 
    "Traveling to new places broadens the mind.", 
    "Winter mornings can be quite chilly.", 
    "They planted flowers in the garden last weekend.",
    "He enjoys playing the guitar in his free time.", 
    "The movie had an unexpected plot twist.", 
    "Taking breaks can improve productivity.", 
    "She carefully wrapped the gift before giving it.", 
    "The mountain trail was challenging but rewarding.", 
    "They discussed the project in detail.", 
    "A good book can transport you to another world.", 
    "The festival was filled with music and laughter.", 
    "She decided to learn how to bake bread.", 
    "The teacher explained the concept clearly.",
    "Writing daily helps improve creativity.", 
    "The baby smiled when it saw its mother.", 
    "A positive attitude can make a big difference.", 
    "They watched the stars from the rooftop.", 
    "The cake turned out delicious.", 
    "The old house had a mysterious charm.", 
    "Learning from mistakes is part of growth.", 
    "The scientist made an important discovery.", 
    "She enjoys walking along the beach at sunset.", 
    "The storm knocked out the power for a few hours.",
    "He always double-checks his work before submitting.", 
    "The museum had an impressive art collection.", 
    "They built a treehouse in their backyard.", 
    "The dog wagged its tail happily.", 
    "She set a goal to run a marathon.", 
    "The bakery sells fresh bread every morning.", 
    "He found a rare coin in his grandfathers collection.", 
    "They organized a surprise party for their friend.", 
    "A good nights sleep is essential for health.", 
    "She enjoys solving complex puzzles."
]
""" for i in range(10):
    # str1 and str2 are two random strings from the list above
    str1 = random.choice(arrayOfSentences)
    str2 = random.choice(arrayOfSentences)
    score = cosine_similarity_score(str1, str2)
    print("Cosine Similarity Score:", score)

"""
