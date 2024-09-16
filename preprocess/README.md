# Preprocessing

## Overview

The preprocessing pipeline consists of two main scripts and a runner script:

1. `preprocess_xhosa.py`: Segments the text and adds paragraph markers.
2. `preprocess_xhosa_all.py`: Cleans the text without segmentation.
3. `run_preprocessing.py`: Runs both preprocessing scripts sequentially.

To replicate our model's processing, run python `run_preprocessing.py`

## Scripts

### preprocess_xhosa.py

This script performs the following operations:
- Cleans the text by removing unusual line terminators.
- Segments the text into sentences.
- Adds '[PAR]' markers at the end of each sentence.

Output files:
- `../data/xhosa_processed/val_xhosa_segmented.txt`
- `../data/xhosa_processed/train_xhosa_segmented.txt`

### preprocess_xhosa_all.py

This script performs minimal preprocessing:
- Cleans the text by removing unusual line terminators.

Output files:
- `../data/xhosa_processed/val_xhosa_all.txt`
- `../data/xhosa_processed/train_xhosa_all.txt`

### run_preprocessing.py

This script runs both `preprocess_xhosa.py` and `preprocess_xhosa_all.py` sequentially.

## Usage

1. Ensure that the raw Xhosa data files are present in the `../data/xhosa_raw/` directory:
   - `valid.xh`
   - `train.xh`

2. Make sure all three Python scripts are in the same directory.

3. Run the preprocessing pipeline:

   ```
   python run_preprocessing.py
   ```

   This will execute both preprocessing scripts for both the validation and training datasets.

4. After running the scripts, you will find the processed files in the `../data/xhosa_processed/` directory.

## Output

The preprocessing pipeline generates four output files:

1. `val_xhosa_segmented.txt`: Validation data with segmented sentences and paragraph markers.
2. `train_xhosa_segmented.txt`: Training data with segmented sentences and paragraph markers.
3. `val_xhosa_all.txt`: Cleaned validation data without segmentation.
4. `train_xhosa_all.txt`: Cleaned training data without segmentation.

These processed files can be used for further natural language processing tasks or model training.

### References
ELC-BERT:
Lucas Georges Gabriel Charpentier and David Samuel. 2023. Not all layers are equally as important: Every Layer Counts BERT. In Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning (CoNLL '23). Association for Computational Linguistics, Singapore, 238–252. https://doi.org/10.18653/v1/2023.conll-babylm.20

WURA:
A. Oladipo, M. Adeyemi, O. Ahia, A. Owodunni, O. Ogundepo, D. Adelani, and J. Lin. 2023. Better Quality Pre-training Data and T5 Models for African Languages. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP '23). Association for Computational Linguistics, Singapore, 158–168. https://doi.org/10.18653/v1/2023.emnlp-main.11