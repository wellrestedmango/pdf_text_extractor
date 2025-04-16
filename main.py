import os
import glob
import argparse
import PyPDF2
from PyPDF2 import PdfReader
from argparse import ArgumentParser


parser = ArgumentParser(prog="main")
parser.add_argument("-src", help="Source directory")
parser.add_argument("-dst", help="Destination directory")
args = parser.parse_args()

src_dir = args.src
dst_dir = args.dst

search_terms = ["social", "Social", "media", "Media", "Mastodon", "mastodon"]

interesting_files = {}
failed_files = []

failed_files_count = 0
found_boring = 0
found_interesting = 0



for p in glob.glob('**', recursive=True, root_dir=src_dir):
    if os.path.isfile(os.path.join(src_dir, p)):
        file_path = f"{os.path.join(src_dir, p)}"
        print(file_path)
        text = ""
        try:
            found_terms = []
            doc = PdfReader(file_path)  # open a document
            for page in range(0, len(doc.pages)):  # iterate the document pages
                curr_page = doc.pages[page]
                text += curr_page.extract_text()# get plain text (is in UTF-8)
            for term in search_terms:
                if term in text:
                    print(f"Found {term} in {p}")
                    found_terms.append(term)
                    break
                else:
                    print("huge bust")
            if not found_terms:
                found_boring += 1
                pass
            else:
                found_interesting += 1
                interesting_files.update({p:found_terms})
                print("still working Eric, don't worry")
        except:
            print("failed")
            failed_files.append(p)
            failed_files_count += 1

print(interesting_files)
print(f'Number of failed files: {failed_files_count}')
print(f'Number of boring files: {found_boring}')
print(f'Number of interesting files: {found_interesting}')






