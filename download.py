import requests
import os


def download_photo(image_url, photo_index, params=None, prefix="image", save_dir="downloaded_images", ext="jpg"):
    os.makedirs(save_dir, exist_ok=True)

    response = requests.get(image_url, params=params)
    response.raise_for_status()

    filename = f"{prefix}_{photo_index}.{ext}"
    file_path = os.path.join(save_dir, filename)

    counter = 1
    while os.path.exists(file_path):
        new_filename = f"{prefix}_{photo_index}_{counter}.{ext}"
        file_path = os.path.join(save_dir, new_filename)
        counter += 1

    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"Скачано: {file_path}")
    return file_path


if __name__ == '__main__':
    pass

