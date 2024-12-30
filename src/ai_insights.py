import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def generate_insights(df):
    client = genai.configure(api_key=getenv("GEMINI_API_KEY"))
    if client is None:
        return "Error generating insights."
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Analyze the following dataset and provide insights:\n{df}"
    response = model.generate_content(prompt)
    return response.text
