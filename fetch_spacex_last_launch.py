import requests
import argparse
from download_gpt import download_photo


def download_launch_photo(launch_id):
        params = {
                "launch_id": launch_id
        }
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        images = response.get('links', {}).get('flickr', {}).get('original', [])

        for photo_index, image_url in enumerate(images):
                download_photo(image_url, photo_index, params)


def main():
        parser = argparse.ArgumentParser(description='Скачивает фотографии запуска ракеты SpaceX  по id запуска')
        parser.add_argument('--id', type=str, default='5eb87d42ffd86e000604b384', help='id запуска SpaceX(по умолчанию:5eb87d42ffd86e000604b384)')
        args = parser.parse_args()
        launch_id = args.id
        download_launch_photo(launch_id)


if __name__ == '__main__':
    main()



