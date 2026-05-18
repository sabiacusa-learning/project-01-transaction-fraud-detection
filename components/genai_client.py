from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DEFAULT_MODEL = os.getenv(
    "MODEL_ID",
    "meta-llama/Meta-Llama-3-70B-Instruct"
)


def get_client():

    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError(
            "HF_TOKEN not found. Add it to your .env file or environment variables."
        )
    return InferenceClient(api_key=token)

def ask_llm(client, prompt, model=DEFAULT_MODEL):
    """
    Send the prompt to the LLM using the chat completion API.
    Returns plain text.
    """
    try:
        response = client.chat_completion(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a fraud detection assistant. "
                        "Analyze the transaction and return:\n"
                        "Fraud Risk: LOW, MEDIUM, or HIGH\n"
                        "Reason: concise explanation"
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_tokens=200,
            temperature=0.2,
            top_p=0.9,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"
