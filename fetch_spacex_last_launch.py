import requests
import argparse
from download import download_launch_photo


def fetch_spacex_last_launch(launch_id):
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        images = response.get('links', {}).get('flickr', {}).get('original', [])

        for index_photo, launch_photo in enumerate(images):
                download_launch_photo(index_photo, launch_photo)

                
def main():
        parser = argparse.ArgumentParser(description='Скачивает фотографии запуска ракеты SpaceX  по id запуска')
        parser.add_argument('--id', type=str, default='5eb87d42ffd86e000604b384', help='id запуска SpaceX(по умолчанию:5eb87d42ffd86e000604b384)')
        args = parser.parse_args()
        launch_id = args.id
        fetch_spacex_last_launch(launch_id)

        
if __name__ == '__main__':
    main()

