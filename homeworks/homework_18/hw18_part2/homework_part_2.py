import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:8080"
base_path = Path(__file__).parent
photo_path = base_path / "photo.jpg"
upload_url = f"{BASE_URL}/upload"

# POST
with open(photo_path, "rb") as file:
    files = {
        "image": file
    }

    response = requests.post(upload_url, files=files)

print("POST:")
print(response.status_code)
print(response.json())

# GET
filename = "photo.jpg"
get_url = f"{BASE_URL}/image/{filename}"

headers = {
    "Content-Type": "text"
}

get_response = requests.get(get_url, headers=headers)

print("\nGET:")
print(get_response.status_code)
print(get_response.json())

# DELETE
delete_url = f"{BASE_URL}/delete/{filename}"
delete_response = requests.delete(delete_url)

print("\nDELETE:")
print(delete_response.status_code)
print(delete_response.json())
