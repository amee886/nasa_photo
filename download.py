import requests
import os


def download_earth_photo(created_url, index_photo,params):
    image_content = requests.get(created_url,params=params)
    image_content.raise_for_status()
    image_file_name = os.path.join('EPIC_images', f"nasa_epic_{index_photo}.png")
    with open(image_file_name, 'wb') as file:
        file.write(image_content.content)


def download_astronomy_photo(image_url, index_photo):
    image_content = requests.get(image_url)
    image_content.raise_for_status()
    image_name = os.path.join('nasa_images', f"nasa_apod_{index_photo}.jpg")
    with open(image_name, 'wb') as file:
        file.write(image_content.content)


def download_launch_photo(index_photo, launch_photo):
    launch_photo_response=requests.get(launch_photo)
    launch_photo_response.raise_for_status()
    with open(f"images_{index_photo}.jpg", "wb") as file:
        file.write(launch_photo_response.content)


if __name__ == '__main__':
    pass
