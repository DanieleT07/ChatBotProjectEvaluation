import re

def refactor_text(input_text):
    # Fix spacing issues (remove unnecessary spaces before punctuation, normalize spaces)
    input_text = re.sub(r'\s+([.,;!?])', r'\1', input_text)  # Remove spaces before punctuation
    input_text = re.sub(r'\s+', ' ', input_text)  # Normalize spaces
    
    # Ensure proper LaTeX formatting (fix escaped characters if needed)
    input_text = input_text.replace('texttt {', '\texttt{').replace('LaTeX {}', 'LaTeX').replace('pdfLaTeX {}', 'pdfLaTeX')
    
    return input_text

# Read input from a file (example)
with open("vault.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
refactored_text = refactor_text(text)

# Save the output
with open("refactored_text.txt", "w", encoding="utf-8") as file:
    file.write(refactored_text)
