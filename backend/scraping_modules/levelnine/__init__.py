import requests
import pymongo
from IPython.testing.decorators import skipif
from dotenv import load_dotenv
import os

load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.levelninesports.com/shop/ski/skis?search=custom&sort=brand&view=40',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-nextjs-data': '1',
}

def get_general_skis(page: int = 1):
    params = {
        'search': 'custom',
        'view': '200',
        'page': page,
    }

    response = requests.get(
        'https://www.levelninesports.com/_next/data/Wisv5atNxXVap3nzPJ_lY/shop/ski/skis.json',
        params=params,
        headers=headers,
    )

    return [product.get('url').replace("https://www.levelninesports.com/", "") for product in response.json()["pageProps"]["initialState"]["products"]]


def get_all_ski_slugs():
    slugs = []
    page = 1

    while True:
        current_request_slugs = get_general_skis(page)
        slugs.extend(current_request_slugs)
        page += 1

        if len(current_request_slugs) != 200:
            break

    return slugs


def get_ski_data(slug: str):
    response = requests.get(
        'https://www.levelninesports.com/_next/data/Wisv5atNxXVap3nzPJ_lY/' + slug + '.json',
        headers=headers,
    )

    return response.json()["pageProps"]["product"]


def upload_ski_to_mongo(ski: dict):
    db = client["product_db"]
    collection = db["levelnine"]

    collection.update_one({"path": ski["path"]}, {"$set": ski}, upsert=True)
