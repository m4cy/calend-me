import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import smtplib

# import json
import os
from json.decoder import JSONDecodeError
from typing import List, Optional
from urllib.error import HTTPError, URLError

import click  # type: ignore
import jsonschema  # type: ignore
from jsonschema import RefResolver
from requests import exceptions  # type: ignore

class MeMailer:
    def __init__(
        self,
        email: str,
        frequency: int
    ):
        self.email = email
        self.frequency = frequency
    
    def fetch_and_parse_file(self, input_path) -> dict:
        data = None
        try:
            resp = requests.get(input_path)
            data = resp.json()
        except:
            print('didnt work')
        return data
