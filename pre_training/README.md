## Pre-training

We make use of the original ELC-BERT cache_dataset.py script to cache our data. We include all the original util files. All pre_training files from the original ELC-BERT repository are available at: https://github.com/ltgoslo/elc-bert/tree/main/pre_training

### Caching the Dataset

To allow for easy replication of our model, we've created a new script `cache_both_datasets.py`. This script runs the original `cache_dataset.py` for both the training and validation segmented files (train_xhosa_segment.txt and val_xhosa_segment.txt) at once. So to replicate our model, run:

```bash
python cache_both_datasets.py
```
Output files are saved at the following paths:
`../data/xhosa_processed/train_xhosa_cached_128.txt`
`../data/xhosa_processed/val_xhosa_cached_128.txt` 


If you need to override any of these defaults, you can run the original `cache_both_datasets.py` script and specify your arguments:

```bash
python cache_both_datasets.py \
    --train_segments_path="../data/custom/train_segmented.txt" \
    --val_segments_path="../data/custom/val_segmented.txt" \
    --tokenizer_path="../tokenizers/custom_tokenizer.json" \
    --sequence_length=256
```
When doing this, make sure to cache both your train_segmented file and your val_segmented file

### References

Lucas Georges Gabriel Charpentier and David Samuel. 2023. Not all layers are equally as important: Every Layer Counts BERT. In Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning (CoNLL '23). Association for Computational Linguistics, Singapore, 238–252. https://doi.org/10.18653/v1/2023.conll-babylm.20