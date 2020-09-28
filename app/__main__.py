
import time
import requests
import os
import dotenv

from appscript import app, mactypes
dotenv.load_dotenv()



def choose_background() -> str:
    """Randomly choose a new image for the background."""
    # TODO:
    UNSPLASH_ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']
    host = 'https://api.unsplash.com'
    endpoint = '/photos/random'
    url = f'{host}{endpoint}' # use Unsplash API to download random image
    headers = {'Authorization': 'Client-ID {}'.format(UNSPLASH_ACCESS_KEY)
}
    response = requests.get(url, headers=headers)
    json_response = response.json()
    link = json_response['urls']['full']
    respond = requests.get(link)
    with open(r'/Users/vadimkorovin/projects/refresh-background/images/Whatever_image.jpg', 'wb') as f:
        f.write(respond.content) # download image in to images dir
    path = '/Users/vadimkorovin/projects/refresh-background/images/Whatever_image.jpg' # download image in to images dir

    return str(path)


def set_background(path: str) -> None:
    # TODO: check v

    app("Finder").desktop_picture.set(mactypes.File(path))


def refresh_background() -> None:
    interval = 60
    while True:
        path = choose_background()
        set_background(path)
        time.sleep(interval)


def main() -> None:
    try:
        refresh_background()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print("Unhandled error: {}".format(err))
        raise


if __name__ == "__main__":
    main()
