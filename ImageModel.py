import requests
from typing import List, Optional, Tuple


from config import API_KEY, API_SECRET

IMAGGA_API_ENDPOINT = "https://api.imagga.com"

class ImageModel:
    def get_image(self, url: str) -> bytes:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content

    def post_image(self, image: bytes) -> Optional[Tuple[List[str], List[float]]]:
        url = f"{IMAGGA_API_ENDPOINT}/v2/tags"
        auth = (API_KEY, API_SECRET)
        files = {"image": image}
        response = requests.post(url, files=files, auth=auth)
    
        # parse the response
        if response.status_code == 200:
            data = response.json()
            tags = [tag["tag"]["en"] for tag in data["result"]["tags"]]
            percentages = [tag["confidence"] for tag in data["result"]["tags"]]
            return tags, percentages  # Returning both tags and percentages as a tuple
        else:
            return None  # Returning None in case of error