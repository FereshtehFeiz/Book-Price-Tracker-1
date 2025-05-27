import requests

def fetch_page(url):
    res = requests.get(url)
    return res.content
    