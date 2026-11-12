from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

history = []  # the whole conversation lives here, in YOUR code

while True:
    question = input("You: ")
    if question.lower().strip() in ("bye", "exit"):
        break

    history.append({"role": "user", "parts": [{"text": question}]})

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=history,  # send everything so far, not just the new question
        config=types.GenerateContentConfig(
            system_instruction="You are a friendly mentor. Keep answers under 3 sentences.",
        ),
    )

    print("AI:", response.text)
    history.append({"role": "model", "parts": [{"text": response.text}]})

    usage = response.usage_metadata
    print(f"[tokens sent: {usage.prompt_token_count}, received: {usage.candidates_token_count}]\n")


