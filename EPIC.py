import requests
import os
from decouple import config
from datetime import datetime
from download_gpt import download_photo


def download_earth_photo(limit, nasa_api_key):
        params={
                "api_key": nasa_api_key
                }
        url_epic = f"https://api.nasa.gov/EPIC/api/natural/images"
        response = requests.get(url_epic,params=params)
        response.raise_for_status()
        gets_dictionary = response.json()
        for photo_index, earth_photo in enumerate(gets_dictionary):
                if photo_index >= limit:
                        break

                image_name = earth_photo.get("image")
                get_date = earth_photo.get("date")
                date_imaging=datetime.strptime(get_date,"%Y-%m-%d %H:%M:%S")
                year_photo=date_imaging.year
                month_photo=date_imaging.month
                day_photo=date_imaging.day
                image_url = f"https://api.nasa.gov/EPIC/archive/natural/{year_photo:04d}/{month_photo:02d}/{day_photo:02d}/png/{image_name}.png"
                download_photo(image_url, photo_index,params)


def main():
    nasa_api_key = config("NASA_API_KEY")
    download_earth_photo(10, nasa_api_key)

    
if __name__ == '__main__':
    main()
