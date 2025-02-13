import json
import ollama
import re
import sys
from collections import defaultdict

def check_response(question, response):
    prompt = f"""
    Given the following question and response, determine if the response plausibly answers the question.
    
    Question: {question}
    Response: {response}
    
    Respond only with one of the following labels:
    - Plausible
    - Partially plausible
    - Not Plausible
    """
    
    result = ollama.chat(model='llama3.1', messages=[{"role": "user", "content": prompt}])
    return result['message']['content'].strip()

def process_file(input_file, log_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()
    
    qa_pairs = re.findall(r'Question:\s*(.*?)\s*Response:\s*(.*?)(?=\nQuestion:|$)', data, re.DOTALL)
    
    with open(log_file, 'w', encoding='utf-8') as log:
        for question, response in qa_pairs:
            plausibility = check_response(question.strip(), response.strip())
            log.write(f"Question: {question.strip()}\nResponse: {response.strip()}\nPlausibility: {plausibility}\n\n")

def evaluate_log(log_file):
    with open(log_file, 'r', encoding='utf-8') as log:
        log_content = log.read()
    
    total = log_content.count("Plausibility:")
    not_plausible = log_content.count("Plausibility: Not Plausible")
    partially_plausible = log_content.count("Plausibility: Partially plausible")
    plausible = total - (not_plausible + partially_plausible)
    
    if total > 0:
        not_plausible_percent = (not_plausible / total) * 100
        partially_plausible_percent = (partially_plausible / total) * 100
        plausible_percent = (plausible / total) * 100
    else:
        not_plausible_percent = partially_plausible_percent = plausible_percent = 0.0
    
    with open(log_file, 'a', encoding='utf-8') as log:
        log.write(f"\nStatistics:\n")
        log.write(f"Total Evaluations: {total}\n")
        log.write(f"Plausible: {plausible} ({plausible_percent:.2f}%)\n")
        log.write(f"Partially Plausible: {partially_plausible} ({partially_plausible_percent:.2f}%)\n")
        log.write(f"Not Plausible: {not_plausible} ({not_plausible_percent:.2f}%)\n")

def compare_logs(log_files):
    question_stats = defaultdict(lambda: {"total": 0, "not_plausible": 0, "partially_plausible": 0})
    
    for log_file in log_files:
        with open(log_file, 'r', encoding='utf-8') as log:
            log_content = log.read()
            qa_pairs = re.findall(r'Question:\s*(.*?)\s*Response:.*?Plausibility:\s*(.*?)(?=\nQuestion:|$)', log_content, re.DOTALL)
            
            for question, plausibility in qa_pairs:
                question = question.strip()
                question_stats[question]["total"] += 1
                if "Not Plausible" in plausibility:
                    question_stats[question]["not_plausible"] += 1
                elif "Partially plausible" in plausibility:
                    question_stats[question]["partially_plausible"] += 1
    
    with open("comparison_log.txt", 'w', encoding='utf-8') as log:
        for question, stats in question_stats.items():
            total = stats["total"]
            not_plausible = stats["not_plausible"]
            partially_plausible = stats["partially_plausible"]
            plausible = total - (not_plausible + partially_plausible)
            
            log.write(f"Question: {question}\n")
            log.write(f"Total Evaluations: {total}\n")
            log.write(f"Plausible: {plausible} ({(plausible / total) * 100:.2f}%)\n")
            log.write(f"Partially Plausible: {partially_plausible} ({(partially_plausible / total) * 100:.2f}%)\n")
            log.write(f"Not Plausible: {not_plausible} ({(not_plausible / total) * 100:.2f}%)\n\n")

def main(mode, *files):
    if mode == "q":
        process_file(files[0], "log.txt")
    elif mode == "e":
        evaluate_log("log.txt")
    elif mode == "c":
        process_file(files[0], "log.txt")
        evaluate_log("log.txt")
    elif mode == "cmp":
        compare_logs(files)
    else:
        print("Invalid mode. Use 'q' for query, 'e' for evaluate, 'c' for complete, or 'cmp' for compare.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <mode> [files...]")
    else:
        main(sys.argv[1], *sys.argv[2:])
