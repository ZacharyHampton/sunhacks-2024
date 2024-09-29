from fastapi import FastAPI, APIRouter
import openai
import pandas as pd
import os
from dotenv import load_dotenv
from pydantic import BaseModel

router = APIRouter()
load_dotenv()

# Load your CSV datasets
books_data = pd.read_csv("data/filtered_2_books.csv")
skis_data = pd.read_csv("data/Skis.csv")
phones_data = pd.read_csv("data/Phones_Sheet.csv")

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


# Helper functions to fetch product recommendations (limiting results to 3 to 5)
def get_books_recommendation(genre="Fantasy"):
    filtered_books = books_data[books_data['specifications.Subjects'].str.contains(genre, case=False, na=False)]
    return filtered_books[['title', 'image_url']].head(5).to_dict(orient='records')  # Limit to 5 results


def get_ski_recommendation():
    beginner_skis = skis_data[
        skis_data['specifications.seo.metaDescription'].str.contains('beginner', case=False, na=False)]
    return beginner_skis[['title', 'image_url']].head(5).to_dict(orient='records')  # Limit to 5 results


def get_phone_recommendation():
    return phones_data[['Model', 'image_url']].head(5).to_dict(orient='records')  # Limit to 5 results


class ChatRequest(BaseModel):
    text: str


# API route to handle chatbot queries
@router.post("/chat")
async def chat_with_gpt(data: ChatRequest):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"The user asked: {data.text}. Based on the following datasets (books, skis, phones), provide appropriate recommendations if relevant:",
            },
        ],
        max_tokens=150,
    )

    # Parse the response from GPT
    gpt_response = response.choices[0].message.content.strip()

    # Logic to provide product recommendations if relevant
    if "book" in data.text.lower():
        recommendations = get_books_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some book recommendations: {recommendations}"}
    elif "ski" in data.text.lower():
        recommendations = get_ski_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some ski recommendations: {recommendations}"}
    elif "phone" in data.text.lower():
        recommendations = get_phone_recommendation()
        return {"response": f"{gpt_response}\n\nHere are some phone recommendations: {recommendations}"}
    else:
        return {"response": gpt_response}