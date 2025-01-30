import requests
import pandas as pd
from config import Config

class APIClient:
    def __init__(self):
        self.headers = {
            "User-Agent": "MemeBot/1.0",
            "Accept": "application/json"
        }

    def get_pump_fun_tokens(self):
        """Real Pump.fun API integration"""
        try:
            response = requests.get(
                Config.PUMP_FUN_TOKENS_URL,
                headers={**self.headers, "Authorization": f"Bearer {Config.PUMP_FUN_API}"}
            )
            return pd.DataFrame(response.json()['tokens'])
        except Exception as e:
            print(f"Pump.fun API Error: {str(e)}")
            return pd.DataFrame()

    def get_gmgn_analysis(self, contract_address):
        """GMGN.ai API integration"""
        try:
            response = requests.post(
                "https://api.gmgn.ai/v1/chain/analysis",
                json={"contract_address": contract_address},
                headers={**self.headers, "X-GMGN-TOKEN": Config.GMGN_API}
            )
            return response.json()
        except Exception as e:
            print(f"GMGN API Error: {str(e)}")
            return {}

    def get_bullx_prediction(self, symbol):
        """BullX.io API integration"""
        try:
            response = requests.get(
                f"https://api.bullx.io/v2/predict/{symbol}",
                headers={**self.headers, "X-API-KEY": Config.BULLX_API}
            )
            return response.json()
        except Exception as e:
            print(f"BullX API Error: {str(e)}")
            return {}
