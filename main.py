import os
import glob
import PyPDF3
import re
import argparse
from argparse import ArgumentParser


parser = ArgumentParser(prog="main")
parser.add_argument("-src", help="Source directory")
parser.add_argument("-dst", help="Destination directory")
args = parser.parse_args()

src_dir = args.src
dst_dir = args.dst

search_terms = ["social", "Social", "media", "Media", "Mastodon", "mastodon"]

for p in glob.glob('**', recursive=True, root_dir=src_dir):
    if os.path.isfile(os.path.join(src_dir, p)):
        file_path = f"{os.path.join(src_dir, p)}"
        print(file_path)
        #with open(file_path, 'r') as pdfFileObj:
        text = ""
        try:
            pdfReader = PyPDF3.PdfFileReader(file_path)
            for i in range(pdfReader.numPages):
                page = pdfReader.pages[i]
                text += f", {page.extractText()}"

            sentence_text = text.split(",")

            for sentence in sentence_text:
                for keyword in search_terms:
                    if keyword in sentence:
                        print(f'keyword: {keyword} found in sentence: {sentence}')

        except:
            print("it didn't work")







