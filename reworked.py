import os
import glob
import argparse
import textract # Changed from PyPDF2
from argparse import ArgumentParser

parser = ArgumentParser(prog="main")
parser.add_argument("-src", help="Source directory")
parser.add_argument("-dst", help="Destination directory")
args = parser.parse_args()

src_dir = args.src
dst_dir = args.dst

#search terms go here
search_terms = ["foo","bar"]

interesting_files = {}
failed_files = []
failed_files_count = 0
found_boring = 0
found_interesting = 0
crawled_files = 0

def extract_text(file_path1):
    try:
        text1 = textract.process(file_path1) #Use textract's pdf processing
        return text1
    except Exception as e:
        print(f"Error processing {file_path1}: {e}")
        return None


for root, _, files in os.walk(src_dir, topdown=True): #changed glob
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        text = extract_text(file_path)
        if text:
            for term in search_terms:
                if term in text.decode('utf-8'):#decode from bytes to string
                    print(f"Found {term} in {file_path}")
                    if file_path not in interesting_files:
                        interesting_files[file_path] = []
                        interesting_files[file_path].append(term)
                    else:
                        print("failed")
                        failed_files.append(file_path)
                        failed_files_count += 1

# Print the results
for key, value in interesting_files.items():
    print(f'{key} : {value}')
print(f'Number of failed files: {failed_files_count}')
print(f'Number of boring files: {found_boring}')
print(f'Number of interesting files: {found_interesting}')


# Write results to file
fout = dst_dir
fo = open(fout, "w")

for key, value in interesting_files.items():
    fo.write(f'{key} >>> {value}\n\n')
fo.close()
