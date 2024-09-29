import random
from urllib.parse import urlparse, parse_qs
import requests
from IPython.core.display_functions import display
from bs4 import BeautifulSoup
from pydantic import BaseModel, AnyUrl
import price_parser
from concurrent.futures import ThreadPoolExecutor
from http.cookiejar import DefaultCookiePolicy
from ..proxies import proxies
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
import pymongo
from pymongo import UpdateOne
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))

session = requests.Session()
session.cookies.set_policy(DefaultCookiePolicy(allowed_domains=[]))
session.headers.update({
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
})
session.proxies = {
    'http': 'http://pkg-lemonstream-country-any:dq9vcsf250klhmzz@gw-us.lemonclub.io:5555',
    'https': 'http://pkg-lemonstream-country-any:dq9vcsf250klhmzz@gw-us.lemonclub.io:5555'
}
session.mount('https://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[429], backoff_factor=1)))


class Platform(BaseModel):
    chipset: str | None = None
    gpu: str | None = None


class Price(BaseModel):
    amount: float
    currency: str
    variant: str
    link: AnyUrl


class Phone(BaseModel):
    url: AnyUrl
    title: str
    image_url: AnyUrl
    platform: Platform
    display_size: float
    camera_resolution: float | None = None
    ram: float | tuple[float, float] | None = None
    battery_size: int | None = None
    colors: list[str]
    prices: list[Price]


class BrandPage(BaseModel):
    phone_urls: list[str]
    next_page_url: str | None = None



def get_all_brands():
    response = session.get('https://www.gsmarena.com/makers.php3')
    soup = BeautifulSoup(response.text, 'html.parser')

    container_element = soup.find('div', {'class': 'brandmenu-v2'})
    return ["https://www.gsmarena.com/" + li.find('a').attrs.get("href") for li in container_element.find_all('li')]


def get_brand_phone_urls(brand_url: str) -> BrandPage:
    response = session.get(brand_url, proxies=random.choice(proxies))
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    next_page_button = None
    if pagination_container := soup.find('div', {'class': 'nav-pages'}):
        next_page_button = pagination_container.find('a', {'title': 'Next page'})

    phone_elements = soup.find('div', {'class': 'makers'}).find_all('li')

    return BrandPage(
        phone_urls=["https://www.gsmarena.com/" + phone_element.find('a').attrs.get('href') for phone_element in phone_elements],
        next_page_url="https://www.gsmarena.com/" + next_page_button.attrs.get('href') if next_page_button else None
    )


def get_phone(url: str) -> Phone:
    response = session.get(url)
    response.raise_for_status()

    if len(response.content) <= 20:  #: invalid response
        return get_phone(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    pricing = []
    if pricing_table_phones := soup.find('table', {'class': 'pricing'}):
        for phone_type_container in pricing_table_phones.find_all('tr'):
            variant = phone_type_container.find('td').text

            for affiliate in phone_type_container.find_all('a'):
                price_raw = affiliate.text
                price = price_parser.parse_price(price_raw)

                pricing.append(Price(
                    amount=price.amount_float,
                    currency=price.currency,
                    variant=variant,
                    link=affiliate.attrs.get('href')
                ))

    ram_raw = None
    if ram_element := soup.find('span', {'data-spec': 'ramsize-hl'}):
        ram_raw = ram_element.text
        if '/' in ram_raw:
            ram_raw = tuple(map(float, ram_raw.split('/')))
        elif "-" in ram_raw:
            ram_raw = tuple(map(float, ram_raw.split('-')))
        else:
            ram_raw = float(ram_raw)

    display_size = None
    if display_element := soup.find('span', {'data-spec': 'displaysize-hl'}):
        if (display_size := display_element.text.replace('"', '')) and display_size != "":
            display_size = float(display_size)

    return Phone(
        url=url,
        title=soup.find('h1', {'data-spec': 'modelname'}).text,
        image_url=soup.find('div', {'class': 'specs-photo-main'}).find('img').attrs.get('src'),
        platform=Platform(
            chipset=chipset_element.text if (chipset_element := soup.find('td', {'data-spec': 'chipset'})) else None,
            gpu=gpu_element.text if (gpu_element := soup.find('td', {'data-spec': 'gpu'})) else None
        ),
        display_size=display_size,
        camera_resolution=float(camera_resolution_element.text) if (camera_resolution_element := soup.find('span', {'data-spec': 'camerapixels-hl'})) else None,
        ram=ram_raw,
        battery_size=int(battery_element.text) if (battery_element := soup.find('span', {'data-spec': 'batsize-hl'})) else None,
        colors=soup.find('td', {'data-spec': 'colors'}).text.split(', '),
        prices=pricing
    )


def get_phones(urls: list[str]) -> list[Phone]:
    phones = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        phones.extend(executor.map(get_phone, urls))

    return phones


def get_phones_from_brand(brand_url: str):
    brand_page = get_brand_phone_urls(brand_url)
    while brand_page.next_page_url:
        phones = get_phones(brand_page.phone_urls)
        yield phones

        brand_page = get_brand_phone_urls(brand_page.next_page_url)


def upload_phones_to_mongo(phones: list[Phone]):
    db = client["product_db"]
    collection = db["gsmarena"]

    queries = [UpdateOne({'url': str(phone.url)}, {'$set': json.loads(phone.model_dump_json())}, upsert=True) for phone in phones]
    collection.bulk_write(queries)

