#This file performs a basic clean, primarily just to remove the line and paragraph separators in the file and save the outputs in the right locations

import os

#remove paragarph and line separator characters
def clean_text(text):
    clean_text = text.replace('\u2028', '').replace('\u2029', '')
    return clean_text

#logic to save files
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    text = clean_text(text)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8', newline='\n') as file:
        file.write(text)

def main():
    input_files = ['../data/xhosa_raw/valid.xh', '../data/xhosa_raw/train.xh']
    output_files = ['../data/xhosa_processed/val_xhosa_all.txt', '../data/xhosa_processed/train_xhosa_all.txt']

    for input_file, output_file in zip(input_files, output_files):
        process_file(input_file, output_file)

if __name__ == "__main__":
    main()