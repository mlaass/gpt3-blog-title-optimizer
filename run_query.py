import json
from google.cloud import bigquery

# specify your service account key file here
key_path = "./bookmachine-bqkey.json"

# construct a BigQuery client object
client = bigquery.Client.from_service_account_json(key_path)


# load SQL script from file
with open('gpt3_input_data.sql', 'r') as file:
    sql = file.read()

# execute the query
query_job = client.query(sql)  # Make an API request.
rows = query_job.result()  # Waits for query to finish

# prepare the data for JSON
data = [dict(row) for row in rows]

# write the data to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file)
