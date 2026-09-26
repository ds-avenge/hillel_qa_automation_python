import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://images-api.nasa.gov"
base_path = Path(__file__).parent
session = requests.Session()

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 100  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = session.get(search_url, params=search_params)

# print(response.status_code)
# print(response.json())

data = response.json()
items = data["collection"]["items"]
nasa_ids = []

for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)
    # print(nasa_ids)

def download_photo(index, nasa_id):
    print(f"[{index}] Processing {nasa_id}")
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = session.get(asset_url)
    # print(asset_response.status_code)
    # print(asset_response.json())

    asset_data = asset_response.json()
    asset_items = asset_data["collection"]["items"]

    image_url = None
    for asset_item in asset_items:
        href = asset_item["href"]
        if href.endswith("~orig.jpg"):
            image_url = href
            break

    if image_url is None:
        print(f"No image found for {nasa_id}")
        return

    image_response = session.get(image_url)

    photo_folder = base_path / "photos"
    photo_folder.mkdir(exist_ok=True)
    photo_name = f"mars_photo{index}.jpg"
    photo_path = photo_folder / photo_name

    with open(photo_path, "wb") as f:
        f.write(image_response.content)

    print(f"Downloaded {photo_name}")

with ThreadPoolExecutor(max_workers=25) as executor:
    for index, nasa_id in enumerate(nasa_ids, start=1):
        executor.submit(download_photo, index, nasa_id)
