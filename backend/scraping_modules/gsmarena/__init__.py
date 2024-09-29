import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, AnyUrl
import price_parser
from concurrent.futures import ThreadPoolExecutor


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.gsmarena.com/alcatel-phones-5.php',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


class Platform(BaseModel):
    chipset: str
    gpu: str


class Phone(BaseModel):
    title: str
    image_url: AnyUrl
    platform: Platform
    display_size: float
    camera_resolution: int | None = None
    ram: float | tuple[float, float]
    battery_size: int
    colors: list[str]
    price_range: tuple[float, float] | None = None





class BrandPage(BaseModel):
    phone_urls: list[str]
    next_page_url: str | None = None



def get_all_brands():
    response = requests.get('https://www.gsmarena.com/makers.php3', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    container_element = soup.find('div', {'class': 'brandmenu-v2'})
    return ["https://www.gsmarena.com/" + li.find('a').attrs.get("href") for li in container_element.find_all('li')]


def get_brand_phone_urls(brand_url: str) -> BrandPage:
    response = requests.get(brand_url, headers=headers)
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
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = None
    if pricing_table_phones := soup.find('table', {'class': 'pricing'}):
        prices = [price_parser.Price.fromstring(element.find("a").text).amount_float for element in pricing_table_phones.find_all("tr")]

    ram_raw = soup.find('span', {'data-spec': 'ramsize-hl'}).text
    if '/' in ram_raw:
        ram_raw = tuple(map(float, ram_raw.split('/')))
    else:
        ram_raw = float(ram_raw)

    return Phone(
        title=soup.find('h1', {'class': 'specs-phone-name-title'}).text,
        image_url=soup.find('div', {'class': 'specs-photo-main'}).find('img').attrs.get('src'),
        platform=Platform(
            chipset=soup.find('td', {'data-spec': 'chipset'}).text,
            gpu=soup.find('td', {'data-spec': 'gpu'}).text
        ),
        display_size=float(soup.find('span', {'data-spec': 'displaysize-hl'}).text.replace('"', '')),
        camera_resolution=int(camera_resolution_element.text) if (camera_resolution_element := soup.find('span', {'data-spec': 'camerapixels-hl'})) else None,
        ram=ram_raw,
        battery_size=int(soup.find('span', {'data-spec': 'batsize-hl'}).text),
        colors=soup.find('td', {'data-spec': 'colors'}).text.split(', '),
        price_range=(min(prices), max(prices)) if prices else None
    )


def get_phones(urls: list[str]) -> list[Phone]:
    phones = []
    with ThreadPoolExecutor() as executor:
        phones.extend(executor.map(get_phone, urls))

    return phones


def get_phones_from_brand(brand_url: str):
    phone_urls = []

    brand_page = get_brand_phone_urls(brand_url)
    while brand_page.next_page_url:
        phone_urls.extend(brand_page.phone_urls)
        brand_page = get_brand_phone_urls(brand_page.next_page_url)

    return get_phones(phone_urls)




