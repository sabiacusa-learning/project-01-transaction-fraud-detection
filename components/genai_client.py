from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
hf_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
hf_chat_model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

def get_client():
    # Replace with your HF token
    return InferenceClient(
        model=hf_chat_model_id,
        token= hf_api_token 
    )

def ask_llm(client, prompt):
    response = client.text_generation(
        prompt,
        max_new_tokens=300,
        temperature=0.3,
        top_p=0.9
    )
    return response
