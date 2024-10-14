import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("LANGCHAIN_API_KEY")
print(api_key)  # This should print your API key
