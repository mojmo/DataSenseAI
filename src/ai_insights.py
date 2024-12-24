import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_insights(df):
    prompt = f"Analyze the following dataset and provide insights:\n{df}"
    response = model.generate_content(prompt)
    return response.text
