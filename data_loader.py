import os
import requests
from git import Repo

#Masakhane organisation's github repos and paths to the isiXhosa data 
REPOS = {
    "ner": {
        "url": "https://github.com/masakhane-io/masakhane-ner.git",
        "path": "MasakhaNER2.0/data/xho",
        "local_dir": "finetune_data/xho/ner"
    },
    "news": {
        "url": "https://github.com/masakhane-io/masakhane-news.git",
        "path": "data/xho",
        "local_dir": "finetune_data/xho/news"
    },
    "pos": {
        "url": "https://github.com/masakhane-io/masakhane-pos.git",
        "path": "data/xho",
        "local_dir": "finetune_data/xho/pos"
    }
}

def clone_and_copy(repo_url, repo_path, local_dir):
    # create temp directory for cloning
    temp_dir = "temp_repo"
    
    try:
        # clone repo
        print(f"Cloning {repo_url}...")
        Repo.clone_from(repo_url, temp_dir)
        
        
        os.makedirs(local_dir, exist_ok=True)
        
        # copy the specific folder from the cloned repo to the local directory
        source_path = os.path.join(temp_dir, repo_path)
        os.system(f"cp -r {source_path}/* {local_dir}")
        
        print(f"Data copied to {local_dir}")
    
    finally:
        #now remove the tempority directory for neatness
        os.system(f"rm -rf {temp_dir}")

def main():
    for name, repo_info in REPOS.items():
        print(f"Processing {name} dataset...")
        
        clone_and_copy(repo_info["url"], repo_info["path"], repo_info["local_dir"])

    print("All datasets downloaded and copied successfully.")

if __name__ == "__main__":
    main()