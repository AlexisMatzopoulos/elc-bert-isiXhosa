## Configs folder

This folder is copied from https://github.com/ltgoslo/elc-bert/tree/main/configs and contains the config files for the original ELC-BERT small and large submissions. We use the ELC-BERT small config for our ELC-BERT isiXhosa model.

```json
{
    "attention_probs_dropout_prob": 0.1,
    "hidden_dropout_prob": 0.1,
    "hidden_size": 384,
    "intermediate_size": 1024,
    "max_position_embeddings": 512,
    "position_bucket_size": 32,
    "num_attention_heads": 6,
    "num_hidden_layers": 12,
    "vocab_size": 6144,
    "layer_norm_eps": 1.0e-7
  }
```

To add a new model parameter simply put a comma to the last line and add on the next line:

```json
    "PARAM_NAME": PARAM_VALUE
```