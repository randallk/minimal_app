import requests
import os

web_url = os.environ.get('WEB_URL', 'http://webserver:8080/')


def test():
    assert requests.get(web_url).content == b'hi'
