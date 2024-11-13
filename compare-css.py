import os
import difflib
from itertools import combinations

def get_similarity(file1_lines, file2_lines):
    matcher = difflib.SequenceMatcher(None, file1_lines, file2_lines)
    return matcher.ratio()

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    similarity = get_similarity(file1_lines, file2_lines)
    return file1, file2, similarity

def find_css_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css') and file not in ['reset.css', 'modern-reset.css', 'reset-typography.css']:
                yield os.path.join(root, file)

def compare_all_css_files(directory):
    css_files = list(find_css_files(directory))
    print(f"CSS files to compare: {css_files}")

    if not css_files or len(css_files) < 2:
        print("Not enough CSS files to compare.")
        return
    
    results = []
    for file1, file2 in combinations(css_files, 2):
        file1, file2, similarity = compare_files(file1, file2)
        results.append((file1, file2, similarity))

    # Calculate average similarity
    total_similarity = sum(similarity for _, _, similarity in results)
    average_similarity = total_similarity / len(results) if results else 0

    # Determine desktop path across different operating systems
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "css-results.txt")

    with open(desktop_path, 'w') as output_file:
        # Write the average similarity at the top
        output_file.write(f"Average Similarity: {average_similarity*100:.2f}%\n\n")
        
        # Sort results by similarity in descending order and write pairwise comparisons
        results.sort(key=lambda x: x[2], reverse=True)
        for file1, file2, similarity in results:
            output_file.write(f"Comparison between {file1} and {file2}:\n")
            output_file.write(f"Similarity: {similarity*100:.2f}%\n\n")

    print(f"Results written to {desktop_path}")

# Prompting the user to input the directory path
directory_path = input("Please enter the path to the directory containing CSS files: ")
compare_all_css_files(directory_path)
