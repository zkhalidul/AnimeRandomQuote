import json
import requests

def main(karakter: str):
    req = requests.get(f'https://animechan.vercel.app/api/quotes/anime?title={karakter}')
    quote = json.loads(req.text)
    return quote

if __name__ == '__main__':
    tokoh = input('input nama karakter> ')
    kuote = main(tokoh)
    for k in kuote:
        for q, v in k.items():
            print('{:<10} : {}'.format(q, v))
