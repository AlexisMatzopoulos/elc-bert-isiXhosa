import torch
import shutil
import os
import argparse
import json

def format_model(input_path, output_folder, finetuning_task):
    # Define task-specific output folder paths
    task_paths = {
        "ner": os.path.join(output_folder, "ner", "ner_models"),
        "pos": os.path.join(output_folder, "pos", "pos_models"),
        "news": os.path.join(output_folder, "news", "news_models")
    }

    # Check if the finetuning task is valid and get the corresponding path
    if finetuning_task not in task_paths:
        print(f"Error: Invalid finetuning task '{finetuning_task}'")
        return

    output_task_folder = task_paths[finetuning_task]

    # Create the task-specific output folder if it doesn't exist
    os.makedirs(output_task_folder, exist_ok=True)

    # Load the checkpoint
    checkpoint = torch.load(input_path, map_location=torch.device('cpu'))

    # Keep only the 'model' parameter
    model_state_dict = checkpoint['model']

    # Save the modified dictionary back to a file
    torch.save(model_state_dict, os.path.join(output_task_folder, 'pytorch_model.bin'))

    # Copy utility files
    util_files_dir = "../util_files"
    files_to_copy = ["config.json", "special_tokens_map.json", "tokenizer.json"]

    for file in files_to_copy:
        src = os.path.join(util_files_dir, file)
        dst = os.path.join(output_task_folder, file)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {file} to {output_task_folder}")
        else:
            print(f"Warning: {file} not found in {util_files_dir}")

    # Update config.json with the correct num_labels
    config_path = os.path.join(output_task_folder, "config.json")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Set num_labels based on the finetuning task
        if finetuning_task == "ner":
            config['num_labels'] = 9
        elif finetuning_task == "pos":
            config['num_labels'] = 17
        elif finetuning_task == "news":
            config['num_labels'] = 7
        else:
            print(f"Warning: Unknown finetuning task '{finetuning_task}'. num_labels not updated.")

        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Updated config.json with num_labels: {config.get('num_labels', 'not set')}")

    print(f"Model formatted and saved in {output_task_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format a PyTorch model checkpoint.")
    parser.add_argument("--input_path", required=True, help="Path to the input checkpoint file")
    parser.add_argument("--output_folder", required=True, help="Name of the output folder")
    parser.add_argument("--finetuning_task", required=True, choices=["ner", "pos", "news"], 
                        help="Specify the finetuning task (ner, pos, or news)")

    args = parser.parse_args()

    format_model(args.input_path, args.output_folder, args.finetuning_task)