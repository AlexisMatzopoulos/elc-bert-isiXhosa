# imports required modules
import subprocess
import argparse

# default paths and values for training, validation, tokenizer, and sequence length
DEFAULT_TRAIN_PATH = "../data/xhosa_processed/train_xhosa_segmented.txt"
DEFAULT_VAL_PATH = "../data/xhosa_processed/val_xhosa_segmented.txt"
DEFAULT_TOKENIZER_PATH = "../tokenizers/tokenizer_xhosa_small.json"
DEFAULT_SEQUENCE_LENGTH = 128

# function to run the dataset caching script with the provided arguments
def run_cache_dataset(segments_path, tokenizer_path, sequence_length):
    command = [
        "python", "cache_dataset.py",  # python command and script
        "--segments_path", segments_path,  # path to segmented dataset
        "--tokenizer_path", tokenizer_path,  # path to tokenizer
        "--sequence_length", str(sequence_length)  # sequence length as string
    ]
    
    print(f"Running: {' '.join(command)}")  # log the full command
    result = subprocess.run(command, capture_output=True, text=True)  # run the command and capture output
    
    if result.returncode == 0:
        print("Caching completed successfully.")  # success message
    else:
        print("Caching failed with error:")  # failure message
        print(result.stderr)  # print error details

# main function to handle argument parsing and trigger caching for train and validation datasets
def main():
    parser = argparse.ArgumentParser(description='Cache both training and validation datasets')  # setup argument parser
    parser.add_argument('--train_segments_path', type=str, default=DEFAULT_TRAIN_PATH, help='Path to the training segmented data file')
    parser.add_argument('--val_segments_path', type=str, default=DEFAULT_VAL_PATH, help='Path to the validation segmented data file')
    parser.add_argument('--tokenizer_path', type=str, default=DEFAULT_TOKENIZER_PATH, help='Path to the tokenizer JSON file')
    parser.add_argument('--sequence_length', type=int, default=DEFAULT_SEQUENCE_LENGTH, help='Sequence length of each cached input sequence')
    
    args = parser.parse_args()  # parse arguments

    print("Caching training dataset...")  # log start of training dataset caching
    run_cache_dataset(args.train_segments_path, args.tokenizer_path, args.sequence_length)  # cache training dataset
    
    print("\nCaching validation dataset...")  # log start of validation dataset caching
    run_cache_dataset(args.val_segments_path, args.tokenizer_path, args.sequence_length)  # cache validation dataset

# ensures the main function is only run if the script is executed directly
if __name__ == "__main__":
    main()