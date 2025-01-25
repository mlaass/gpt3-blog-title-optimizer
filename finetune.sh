#!/bin/bash
echo $OPENAI_API_KEY
openai api fine_tunes.create \
-t train.jsonl \
-v validate.jsonl \
-m "babbage" \
--compute_classification_metrics \
--classification_n_classes 2 \
--classification_positive_class " good" \
--n_epochs 4 \
--batch_size 256