from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create the fine-tune
response = openai.FineTune.create(
    training_file="train.jsonl",
    validation_file="validate.jsonl",
    model="davinci-002",
    compute_classification_metrics=True,
    classification_n_classes=2,
    classification_positive_class=" good",
    n_epochs=4,
    batch_size=256
)

# Print the response to stdout
print(response)
