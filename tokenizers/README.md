## Tokenizers Folder

This folder contains both the script to create your own tokenizer as well as the created tokenizers. The tokenizers are created as BPE tokenizers. We use the create_tokenizer.py file from the original ELC-BERT repository (https://github.com/ltgoslo/elc-bert/) to create our tokenizer file.

To replicate our model, use the following arguments: 
```bash
python create_tokenizer.py \
    --input_path="../data/xhosa_processed/train_xhosa_all.txt" \
    --vocab_path="tokenizer_xhosa_small.json" \
    --vocab_size=6144 \
    --min_frequency=10
```

Otherwise, if you are training a different model, use this as an args guide:

```bash
python create_tokenizer.py \
    --input_path="PATH_TO_DATA_FILE" \
    --vocab_path="PATH_TO_WHERE_TO_SAVE_TOKENIZER_FILE" \
    --vocab_size=MAX_VOCABULARY_SIZE \
    --min_frequency=MINIMUM_FREQUENCY_OF_TOKEN_TO_BE_INCLUDED_IN_VOCABULARY
```

We use a vocab_size of 6144 as this was the vocab size used in ELC-BERT's small-strict winning submission

### References

Lucas Georges Gabriel Charpentier and David Samuel. 2023. Not all layers are equally as important: Every Layer Counts BERT. In Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning (CoNLL '23). Association for Computational Linguistics, Singapore, 238–252. https://doi.org/10.18653/v1/2023.conll-babylm.20
