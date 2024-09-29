from distutils.command.upload import upload

from .. import get_all_brands, get_brand_phone_urls, get_phone, get_phones_from_brand, upload_phones_to_mongo

def tests_get_all_brands():
    brands = get_all_brands()

    assert len(brands) > 0


def tests_get_brand_phone_urls():
    brand_page = get_brand_phone_urls("https://www.gsmarena.com/samsung-phones-9.php")

    assert len(brand_page.phone_urls) > 0


def tests_get_phone():
    phone = get_phone("https://www.gsmarena.com/samsung_galaxy_s24_fe-13262.php")

    assert phone is not None


def tests_get_phones_from_brand():
    for phones in get_phones_from_brand("https://www.gsmarena.com/oneplus-phones-95.php"):
        assert len(phones) > 0

        upload_phones_to_mongo(phones)


