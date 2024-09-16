import os

#function splits text into sentences based on punctuations
def segment_text(text):
    
    text = text.replace('\n', ' ')
    
    
    sentence_endings = {'.', '!', '?', '"'}  # punctuation that will indicate the end of a sentence
    segmented_sentences = []  
    sentence = []  

    # iterate over each character in text, and 
    for char in text:
        sentence.append(char)  # Add character to the current sentence
        
        # if the current character is a sentence-ending punctuation, and the next character is a space
        if char in sentence_endings:
            # Check if the next character is a space or if we're at the end of the text
            if len(sentence) >= 2 and sentence[-2].isspace():
                continue  #ignores ellipses (and other sitautions where the punctuation  is followed by a space)
            # join and add the characters and words to form sentences
            full_sentence = ''.join(sentence).strip() + ' [PAR]'
            segmented_sentences.append(full_sentence)  # Add to list of sentences
            sentence = []  
    
    # add any leftover sentences
    if sentence:
        segmented_sentences.append(''.join(sentence).strip() + ' [PAR]')
    
    # returns each of the segmented_sentences on a new line
    return '\n'.join(segmented_sentences)

# removes hidden line separator and pg separator characters
def clean_text(text):
    
    clean_text = text.replace('\u2028', '').replace('\u2029', '')
    return clean_text


def process_file(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()


    text = clean_text(text)
    segmented_text = segment_text(text)

    #handle output dir
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    #ensure correct encoding
    with open(output_file, 'w', encoding='utf-8', newline='\n') as file:
        file.write(segmented_text)


def main():
    #specify input and output files
    input_files = ['../data/xhosa_raw/valid.xh', '../data/xhosa_raw/train.xh']
    output_files = ['../data/xhosa_processed/val_xhosa_segmented.txt', '../data/xhosa_processed/train_xhosa_segmented.txt']

    
    for input_file, output_file in zip(input_files, output_files):
        process_file(input_file, output_file)


if __name__ == "__main__":
    main()