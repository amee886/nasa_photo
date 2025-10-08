import requests
import os
from decouple import config
from urllib.parse import urlsplit
from download_gpt import download_photo


def download_astronomy_photo(nasa_api_key, count):
        params = {
                "api_key": nasa_api_key,
                "count": count
        }
        url = f'https://api.nasa.gov/planetary/apod'
        response = requests.get(url, params=params)
        response.raise_for_status()
        gets_dictionary = response.json()
        for photo_index, astronomy_photo in enumerate(gets_dictionary):
            image_url = astronomy_photo.get('url')
            if image_url and (image_url.endswith(".jpg") or image_url.endswith(".png")):
                download_photo(image_url, photo_index,params)


def main():
        count = 30
        nasa_api_key = config("NASA_API_KEY")
        download_astronomy_photo(nasa_api_key, count)

        
if __name__ == '__main__':
    main()

