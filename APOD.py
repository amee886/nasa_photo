import requests
import os
from decouple import config
from urllib.parse import urlsplit


def APOD(nasa_api_key):
        url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&count=30'
        nasa_apod = "https://apod.nasa.gov/apod/image/2506/IC2177SeagullLRGB-APOD2048.jpg"
        response = requests.get(url)
        data = response.json()
        os.makedirs('nasa_images', exist_ok=True)
        for idx, item in enumerate(data):
            image_url = item.get('url')
            if image_url and (image_url.endswith(".jpg") or image_url.endswith(".png")):
                image_data = requests.get(image_url).content
                image_name = os.path.join('nasa_images', f"nasa_apod_{idx}.jpg")
                with open(image_name, 'wb') as file:
                    file.write(image_data)
        nasa_apod_split = urlsplit(nasa_apod)
        nasa_apod_path = nasa_apod_split.path
        nasa_apod_split = os.path.splitext(nasa_apod_path)
        print(nasa_apod_split[1])

        
def main():
        nasa_api_key = config("NASA_API_KEY")
        APOD(nasa_api_key)

        
if __name__ == '__main__':
    main()

