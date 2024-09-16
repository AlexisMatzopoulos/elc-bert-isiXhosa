## Training the Model

After preprocessing and caching the dataset, you can train the ELC-BERT model using the `train_elc_bert_xhosa_with_validatino.py` script. This script adapts the `train_elc_bert_base.py` file from the original ELC-BERT repository (available at: https://github.com/ltgoslo/elc-bert/blob/main/train_elc_bert_base.py). 

 Below are instructions for both custom parameter settings and replicating our specific model.

### Replicating Our Model

To replicate our ELC-BERT isiXhosa language model, use the following command:

```bash
python train_elc_bert_base_xhosa_with_validation.py \
    --input_path="../data/xhosa_processed/train_xhosa_cached_128.txt" \
    --validation_path="../data/xhosa_processed/val_xhosa_cached_128.txt" \
    --config_file="../configs/small.json" \
    --output_dir="../checkpoints/elc_bert_base_xhosa/your_model_name" \
    --vocab_path="../tokenizers/tokenizer_xhosa_small.json" \
    --optimizer="lamb" \
    --scheduler="cosine" \
    --seq_length=128 \
    --batch_size=128 \
    --learning_rate=5e-4 \
    --max_steps=469000 \
    --long_after=1 \
    --warmup_proportion=0.016 \
    --seed=42 \
    --log_freq=10 \
    --mask_p=0.15 \
    --short_p=0.1 \
    --weight_decay=0.1 \
    --max_gradient=2.0 \
    --gradient_accumulation=1 \
    --label_smoothing=0 \
    --wandb_entity="WANDB_ENTITY_NAME" \
    --wandb_name="WANDB_RUN_NAME" \
    --wandb_project="WANDB_PROJECT_NAME"
    &>> traininglog
```

For 20 epochs: set max_steps to 46900
For 100 epochs: set max_steps to 234500
For 200 epochs: set max_steps to 469000
For 500 epochs: set max_steps to 1172500

### General Usage

You can customize the training process by adjusting various parameters. Here's the general format for running the training script:

```bash
python train_elc_bert_xhosa_with_validation.py \
    --input_path="PATH_TO_CACHED_DATA" \
    --validation_path="PATH_TO_VALIDATION_DATA" \
    --config_file="PATH_TO_CONFIG_FILE" \
    --output_dir="PATH_TO_OUTPUT_DIR" \
    --vocab_path="PATH_TO_TOKENIZER_FILE" \
    --checkpoint_path="PATH_TO_MODEL_CHECKPOINT" \ # (Optional, to continue training)
    --optimizer="NAME_OF_OPTIMIZER" \ # Options: lamb, adamw
    --scheduler="NAME_OF_SCHEDULER" \ # (Not implemented) Options: cosine
    --seq_length=MAX_SEQUENCE_LENGTH \
    --batch_size=TRAINING_BATCH_SIZE \
    --learning_rate=MAX_TRAINING_LEARNING_RATE \
    --max_steps=NUMBER_OF_TRAINING_STEPS \
    --long_after=FRACTION_AFTER_WHICH_TO_4x_SEQUENCE_LENGTH \
    --warmup_proportion=FRACTION_OF_TRAINING_STEPS_FOR_WARMUP \
    --seed=RANDOMIZATION_SEED \
    --log_freq=LOSS_LOGGING_FREQUENCY \ # For WANDB, unused
    --mask_p=TOKEN_MASKING_PROBABILITY \
    --short_p=PROBABILITY_OF_SHORTENING_SEQUENCE \
    --weight_decay=FRACTION_OF_WEIGHT_DECAY \
    --max_gradient=MAX_GRADIENT_BEFORE_CLIPPING \
    --gradient_accumulation=NUMBER_GRADIENT_ACCUMULATION_STEPS \
    --label_smoothing=CROSS_ENTROPY_LABEL_SMOOTHING \
    --wandb_entity="WANDB_ENTITY_NAME" \
    --wandb_name="WANDB_RUN_NAME" \
    --wandb_project="WANDB_PROJECT_NAME"
```
### Full list of changes

Full list of changes:
- Adapted save() function to save labeled checkpoint files at specified frequencies
- Added validate() function to calculate validation loss
- Created and implemented create_val_dataloader() for validation data loading
- Integrated validation process into the main training loop
- Extended Weights & Biases (wandb) logging to validation metrics
- Introduced --validation_path argument for specifying validation data
- Updated checkpoint saving frequency to every 20 epochs and at the last step

### Notes

- The `&>> traininglog` at the end of the command redirects both standard output and standard error to a log file. You can modify this part if you prefer different logging behavior, or remove it if you want logs to appear in the terminal.
- If you're using Weights & Biases (wandb), replace the `wandb_entity`, `wandb_name`, and `wandb_project` parameters with your own values.

### References

Lucas Georges Gabriel Charpentier and David Samuel. 2023. Not all layers are equally as important: Every Layer Counts BERT. In Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning (CoNLL '23). Association for Computational Linguistics, Singapore, 238–252. https://doi.org/10.18653/v1/2023.conll-babylm.20


