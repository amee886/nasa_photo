import os
from decouple import config
from datetime import datetime
from download import download_earth_photo


def earth_polychromatic_imaging_camera(limit, nasa_api_key):
        params={
                "api_key": nasa_api_key
                }
        url_epic = f"https://api.nasa.gov/EPIC/api/natural/images"
        response = requests.get(url_epic,params=params)
        response.raise_for_status()
        json_information = response.json()
        os.makedirs("EPIC_images", exist_ok=True)
        for index_photo, earth_photo in enumerate(json_information):
                if index_photo >= limit:
                        break

                image_name = earth_photo.get("image")
                get_date = earth_photo.get("date")
                date_imaging=datetime.strptime(get_date,"%Y-%m-%d %H:%M:%S")
                year_photo=date_imaging.year
                month_photo=date_imaging.month
                day_photo=date_imaging.day
                params={
                        "api_key": nasa_api_key
                }
                created_url = f"https://api.nasa.gov/EPIC/archive/natural/{year_photo:04d}/{month_photo:02d}/{day_photo:02d}/png/{image_name}.png"
                download_earth_photo(created_url, index_photo,params)


def main():
    nasa_api_key = config("NASA_API_KEY")
    earth_polychromatic_imaging_camera(10, nasa_api_key)


if __name__ == '__main__':
    main()
