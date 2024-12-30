import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv
import google.auth.exceptions

load_dotenv()


def generate_insights(df):
    if google.auth.exceptions.DefaultCredentialsError(getenv("GEMINI_API_KEY")) is None:
        return "Error generating insights."

    genai.configure(api_key=getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Analyze the following dataset and provide insights:\n{df}"
    response = model.generate_content(prompt)
    return response.text
