# Python 3
# pip3 installl pyJwt
import jwt 
import uuid
import hashlib
import time
from urllib.parse import urlencode
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

accessKey = os.getenv('accessKeyBuy')
secretKey = os.getenv('secretKeyBuy')
apiUrl = 'https://api.bithumb.com'

# Set API parameters
requestBody = dict( market='KRW-HUMA', side='bid', volume=133, price=45.1, ord_type='limit' )

# Generate access token
query = urlencode(requestBody).encode()
hash = hashlib.sha512()
hash.update(query)
query_hash = hash.hexdigest()
payload = {
    'access_key': accessKey,
    'nonce': str(uuid.uuid4()),
    'timestamp': round(time.time() * 1000), 
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}   
jwt_token = jwt.encode(payload, secretKey)
authorization_token = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization_token,
  'Content-Type': 'application/json'
}

try:
    # Call API
    response = requests.post(apiUrl + '/v1/orders', data=json.dumps(requestBody), headers=headers)
    # handle to success or fail
    print(response.status_code)
    print(response.json())
except Exception as err:
    # handle exception
    print(err)
# Note: The above code is for placing a buy order on Bithumb using the API.
# Make sure to replace the market, volume, and price with your desired values.