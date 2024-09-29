from fastapi import FastAPI
import openai
import pandas as pd
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

# Load your CSV datasets
books_data = pd.read_csv("sunhacks-2024/backend/api/core/ragmodel/filtered_2_books.csv")
skis_data = pd.read_csv("sunhacks-2024/backend/api/core/ragmodel/Skis.csv")
phones_data = pd.read_csv("sunhacks-2024/backend/api/core/ragmodel/Phones_Sheet.csv")

# Configure OpenAI API
openai.api_key = os.getenv("openai_api_key")

# Helper functions to fetch product recommendations
def get_books_recommendation(genre="Fantasy"):
    filtered_books = books_data[books_data['specifications.Subjects'].str.contains(genre, case=False, na=False)]
    return filtered_books[['title', 'url']].to_dict(orient='records')

def get_ski_recommendation():
    beginner_skis = skis_data[skis_data['specifications.seo.metaDescription'].str.contains('beginner', case=False, na=False)]
    return beginner_skis[['title', 'url']].to_dict(orient='records')

def get_phone_recommendation():
    return phones_data[['Model', 'Price']].to_dict(orient='records')

# API route to handle chatbot queries
@app.post("/chat")
async def chat_with_gpt(user_input: str):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"The user asked: {user_input}. Based on the following datasets (books, skis, phones), provide appropriate recommendations if relevant:",
        max_tokens=150,
    )
    
    # Parse the response from GPT
    gpt_response = response.choices[0].text.strip()

    # Logic to provide product recommendations if relevant
    if "book" in user_input.lower():
        recommendations = get_books_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some book recommendations: {recommendations}"}
    elif "ski" in user_input.lower():
        recommendations = get_ski_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some ski recommendations: {recommendations}"}
    elif "phone" in user_input.lower():
        recommendations = get_phone_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some phone recommendations: {recommendations}"}
    else:
        return {"response": gpt_response}
