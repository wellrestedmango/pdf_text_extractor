import os
import glob
import re
import argparse
import pymupdf
from pymupdf import get_text
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

interesting_files = []

file_dict = {}

for p in glob.glob('**', recursive=True, root_dir=src_dir):
    if os.path.isfile(os.path.join(src_dir, p)):
        file_path = f"{os.path.join(src_dir, p)}"
        print(file_path)
        file_dict[p] = []
        #with open(file_path, 'r') as pdfFileObj:
        text = ""
        try:
            doc = PdfReader(file_path)  # open a document
            for page in range(0, len(doc.pages)):  # iterate the document pages
                curr_page = doc.pages[page]
                text += curr_page.extract_text()# get plain text (is in UTF-8)
            for term in search_terms:
                if term in text:
                    print(f"Found {term} in {p}")
                    file_dict[p].append(term)
                    break
                else:
                    print("huge bust")
        except:
            print("failed")

print(file_dict)






