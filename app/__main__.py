import random
import time

from appscript import app, mactypes

from .common import IMAGES_PATH


def choose_background() -> str:
    """Randomly choose a new image for the background."""
    paths = list(IMAGES_PATH.iterdir())
    path = random.choice(paths)
    return str(path)


def set_background(path: str) -> None:
    # TODO: check
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
