import requests
from config import Config

class HttpClient:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.base_url = cfg.base_url
        self.key = cfg.api_key

    def urlify(func):
        def wrapper(input_str):
            input_str = input_str.replace(" ", "%20")
            func(input_str)
        return wrapper

    def __request_data(self, url):
        response = requests.get(url)
        data = response.json()
        return data
    
    @urlify
    def request_symbol_data(self, symbol):
        return self.__request_data(f"{self.base_url}/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.key}")