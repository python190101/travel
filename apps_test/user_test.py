import requests
from unittest import TestCase

class AddressTest(TestCase):
    def test_add(self):
        url = 'http://localhost:8001/register/'
        data = {"p_num": "18562792736",
                "vzm":3783,
                "password":123}
        resp = requests.post(url, json=data)
        print(resp.json())

