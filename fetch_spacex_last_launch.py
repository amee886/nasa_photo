import requests
import os
from decouple import config
from urllib.parse import urlsplit
from download import download_astronomy_photo


def astronomy_picture_of_the_day(nasa_api_key, count):
        params = {
                "api_key": nasa_api_key,
                "count": count
        }
        url = f'https://api.nasa.gov/planetary/apod'
        nasa_apod = "https://apod.nasa.gov/apod/image/2506/IC2177SeagullLRGB-APOD2048.jpg"
        response = requests.get(url, params=params)
        response.raise_for_status()
        json_information = response.json()
        os.makedirs('nasa_images', exist_ok=True)
        for index_photo, astronomy_photo in enumerate(json_information):
            image_url = astronomy_photo.get('url')
            if image_url and (image_url.endswith(".jpg") or image_url.endswith(".png")):
                download_astronomy_photo(image_url, index_photo)


def main():
        count = 30
        nasa_api_key = config("NASA_API_KEY")
        astronomy_picture_of_the_day(nasa_api_key, count)

        
if __name__ == '__main__':
    main()

