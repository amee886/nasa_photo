import requests
import argparse


def fetch_spacex_last_launch(launch_id):
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        images = response.get('links', {}).get('flickr', {}).get('original', [])

        for idx,img in enumerate(images):
            print(img)
            img_response=requests.get(img).content
            with open(f"images_{idx}.jpg", "wb") as file:
                file.write(img_response)

                
def main():
        parser = argparse.ArgumentParser(description='id запуска ракеты SpaceX')
        parser.add_argument('id', type=str, help='id запуска SpaceX')
        args = parser.parse_args()
        launch_id=args.id
        fetch_spacex_last_launch(launch_id)

        
if __name__ == '__main__':
    main()
