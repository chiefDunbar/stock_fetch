from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

kite = KiteConnect(api_key=os.getenv('API_KEY'))
print(f'Login Link: {kite.login_url()}')

