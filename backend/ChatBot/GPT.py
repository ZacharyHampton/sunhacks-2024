from fastapi import FastAPI, Request
import openai
from pymongo import MongoClient

app = FastAPI()

# Initialize MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['phone_database']
collection = db['phones']

# OpenAI API key
openai.api_key = "your_openai_api_key"

@app.post("/chatbot")
async def chatbot(request: Request):
    user_input = (await request.json()).get("message")
    
    # GPT-4 prompt to extract preferences
    prompt = f"""
    You're a phone recommendation assistant. Based on this user's message, extract key phone preferences: battery size, price, RAM, display size, and other specs.
    User: {user_input}
    
    Return the filters as JSON format:
    {{
        "battery_size": "minimum_battery_in_mAh",
        "price_max": "maximum_price_in_$",
        "ram": "minimum_ram_in_GB",
        "display_size": "minimum_display_size_in_inches"
    }}
    """
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=100
    )
    
    preferences = eval(response['choices'][0]['text'].strip())
    
    # Build MongoDB query based on preferences
    query = {}
    
    if "battery_size" in preferences:
        query["battery_size"] = {"$gte": int(preferences["battery_size"])}
    if "price_max" in preferences:
        query["prices.amount"] = {"$lte": float(preferences["price_max"])}
    if "ram" in preferences:
        query["ram"] = {"$gte": float(preferences["ram"])}
    if "display_size" in preferences:
        query["display_size"] = {"$gte": float(preferences["display_size"])}

    # Retrieve phones from MongoDB matching the query
    phones = collection.find(query).limit(3)

    # Format and return phone data
    results = []
    for phone in phones:
        results.append({
            "title": phone["title"],
            "battery_size": phone["battery_size"],
            "ram": phone["ram"],
            "price": phone["prices"][0]["amount"],
            "image_url": phone["image_url"],
            "url": phone["url"]
        })

    return {"results": results}
