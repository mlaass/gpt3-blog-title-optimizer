import json
import random

JSONL=True

# load the data
with open('output.json', 'r') as file:
    data = json.load(file)

# split the data into good and bad
data_good = [d for d in data if d['completion'] == ' good']
data_bad = [d for d in data if d['completion'] == ' bad']

# shuffle the data
random.shuffle(data_good)
random.shuffle(data_bad)

# calculate the split indices
split_index_good = int(0.7 * len(data_good))
split_index_bad = int(0.7 * len(data_bad))

# split the data into train and validate
train = data_good[:split_index_good] + data_bad[:split_index_bad]
validate = data_good[split_index_good:] + data_bad[split_index_bad:]

# shuffle the data again to mix good and bad
random.shuffle(train)
random.shuffle(validate)
if JSONL:
    # save the data to jsonl
  with open('train.jsonl', 'w') as file:
      for item in train:
          file.write(json.dumps(item) + '\n')

  with open('validate.jsonl', 'w') as file:
      for item in validate:
          file.write(json.dumps(item) + '\n')

else:
  # save the data as json
  with open('train.json', 'w') as file:
      json.dump(train, file)
  with open('validate.json', 'w') as file:
      json.dump(validate, file)
