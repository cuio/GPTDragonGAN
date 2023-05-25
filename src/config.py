from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get the OpenAI secret key
secret_key = os.getenv("OPENAI_SECRET_KEY")

# Now you can use the secret_key to interact with the OpenAI API
