import requests
import os
from decouple import config


def EPIC(limit, nasa_api_key):
        url_epic = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_api_key}"
        response = requests.get(url_epic)
        response_data = response.json()
        os.makedirs("EPIC_images", exist_ok=True)
        for idx, item in enumerate(response_data):
                if idx >= limit:
                        break

                image_name = item.get("image")
                date = item.get("date")
                year, month, day = date.split()[0].split('-')
                created_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png?api_key={nasa_api_key}"
                image_data = requests.get(created_url).content
                image_name = os.path.join('EPIC_images', f"nasa_epic_{idx}.png")
                with open(image_name, 'wb') as file:
                    file.write(image_data)


def main():
    nasa_api_key = config("NASA_API_KEY")
    EPIC(10, nasa_api_key)


if __name__ == '__main__':
    main()
