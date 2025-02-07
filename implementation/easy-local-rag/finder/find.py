import re

import re

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
    """
    Given a list of line numbers and a file path, return the corresponding lines from the file.
    
    :param line_numbers: List of integers representing line numbers (1-based index)
    :param file_path: Path to the file
    :return: List of strings containing the corresponding lines
    """
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


if __name__ == "__main__":
    file_path = "text.txt"
    input_string = "ciao, mi server in 123 e il A132 e 149"
    line_numbers = find_matching_lines(file_path, input_string)
    lines = get_lines_from_file(line_numbers, file_path)
    print(line_numbers)
    print(lines)