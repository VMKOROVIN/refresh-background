import requests
import os
import dotenv
from pprint import pprint

from .common import IMAGES_PATH

dotenv.load_dotenv()

UNSPLASH_ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']


host = 'https://api.unsplash.com'
endpoint = '/photos/random'
url = f'{host}{endpoint}'


headers = {
    'Authorization': 'Client-ID {}'.format(UNSPLASH_ACCESS_KEY)
}
params = {
    'query': 'halloween',
}
response = requests.get(url, params=params,headers=headers)
json_response = response.json()
link = json_response['urls']['full']
respond = requests.get(link)
paths = list(IMAGES_PATH.iterdir())
print(max(paths))


with open (r'/Users/vadimkorovin/projects/refresh-background/images/Whatever_image.jpg', 'wb') as f:
    f.write(respond.content)

    print(response.status_code)
    pprint(response.json())
