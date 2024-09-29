from .. import get_general_skis, get_ski_data, upload_ski_to_mongo, get_all_ski_slugs
from concurrent.futures import ThreadPoolExecutor, as_completed


def tests_get_general_skis():
    results = get_general_skis()

    assert len(results) > 0


def tests_get_ski_data():
    result = get_ski_data('product/atomic-bent-100-skis-2024')

    assert result is not None


def tests_import_all_ski_data():
    slugs = get_all_ski_slugs()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_ski_data, slug) for slug in slugs]

        for future in as_completed(futures):
            ski = future.result()
            upload_ski_to_mongo(ski)
