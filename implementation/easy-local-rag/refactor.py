import re
import sys

def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Apply transformations
    text = re.sub(r"^(\d [A-Z][A-Z])", r"æ\1", text, flags=re.MULTILINE)
    text = re.sub(r"^(\d\.\d [A-Z]|\d\.\d\.\d [A-Z]|\d\.\d\.\d\d [A-Z])", r"ç\1", text, flags=re.MULTILINE)
    text = re.sub(r"^(A\d{3} |A\d{3}/\d{3})", r"Ħ\1", text, flags=re.MULTILINE)
    text = text.replace("\n", " ")
    text = re.sub(r"[Ħçæ]", "\n", text)

    # Write the processed text back to the same file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        process_text(sys.argv[1])
