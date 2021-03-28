import cbpro
import os

key = os.getenv('CBPRO_KEY')
b64secret = os.getenv('CBPRO_SECRET')
passphrase = os.getenv('CBPRO_PASS')

cbp_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
cbp_client.place_market_order(product_id='BTC-USD', 
                               side='buy', 
                               funds='20.00')
