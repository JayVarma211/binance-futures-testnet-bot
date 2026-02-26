import os
from dotenv import load_dotenv
from binance.client import Client


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API_KEY or API_SECRET not found in .env file")

        self.client = Client(api_key, api_secret)

        # IMPORTANT: Use Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, params: dict):
        return self.client.futures_create_order(**params)