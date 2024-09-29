import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client["product_db"]