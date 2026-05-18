from components.genai_client import get_client, ask_llm

client = get_client()

prompt = "Transaction: Amount $9,800 at midnight from a new foreign location."

response = ask_llm(client, prompt)
print(response)