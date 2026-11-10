from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

question = input("Ask something: ")

response = client.models.generate_content(
model="gemini-3.1-flash-lite",
    contents=question,
)

print(response.text)