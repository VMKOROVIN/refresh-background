import time
import requests

from appscript import app, mactypes

from app.common import IMAGES_PATH, UNSPLASH_ACCESS_KEY


def fetch_wallpaper():
    """Randomly fetches wallpaper from unsplash.com through api."""
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": "Client-ID {}".format(UNSPLASH_ACCESS_KEY)}

    response = requests.get(url, headers=headers)
    return response


def store_wallpaper(response: requests.Response) -> str:
    """Downloads random image to the internal folder."""
    image = response.json()  # dict
    image_link = image["urls"]["full"]
    image_id = image["id"]

    response = requests.get(image_link)
    image_content = response.content
    filename = f"{image_id}.jpg"
    image_path = IMAGES_PATH / filename

    with open(image_path, "wb") as jpg_file:
        jpg_file.write(image_content)

    return str(image_path)


def set_background(image_path: str) -> None:
    """Sets the new wallpaper as a desktop background."""
    app("Finder").desktop_picture.set(mactypes.File(image_path))


def refresh_background() -> None:
    """Refreshes background in a set time period."""
    interval = 10
    while True:
        response = fetch_wallpaper()
        image_path = store_wallpaper(response)
        set_background(image_path)
        time.sleep(interval)


def main() -> None:
    try:
        refresh_background()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
