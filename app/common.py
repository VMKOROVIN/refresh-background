import pathlib
import os

import dotenv

dotenv.load_dotenv()


ROOT_PATH = pathlib.Path(__file__).parents[1]
IMAGES_PATH = ROOT_PATH / "images"

UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]

# Check paths
IMAGES_PATH.mkdir(exist_ok=True)
