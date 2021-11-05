import requests
import json

req = requests.get('https://animechan.vercel.app/api/random').text
anime = json.loads(req)
for k, v, in anime.items():
    print('{:<10} : {}'.format(k, v))
