import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    PUMP_FUN_API = os.getenv("PUMP_FUN_API")
    RUGCHECK_API = os.getenv("RUGCHECK_API")
    TWEETSCOUT_API = os.getenv("TWEETSCOUT_API")
    GMGN_API = os.getenv("GMGN_API")
    BULLX_API = os.getenv("BULLX_API")
    
    # Wallet
    WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")
    
    # Trading Parameters
    RISK_THRESHOLD = 65
    STOP_LOSS = 0.15  # 15%
    TAKE_PROFIT = 0.30  # 30%
    
    # Pump.fun API Endpoints
    PUMP_FUN_TOKENS_URL = "https://api.pump.fun/tokens"
    PUMP_FUN_HISTORY_URL = "https://api.pump.fun/history"
