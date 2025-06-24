# Python 3
# pip3 installl pyJwt
import jwt 
import uuid
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

accessKey = os.getenv('accessKey')
secretKey = os.getenv('secretKey')

# Set API parameters
accessKey = accessKey
secretKey = secretKey
apiUrl = 'https://api.bithumb.com'

# Generate access token
payload = {
    'access_key': accessKey,
    'nonce': str(uuid.uuid4()),
    'timestamp': round(time.time() * 1000)
}
jwt_token = jwt.encode(payload, secretKey)
authorization_token = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization_token
}

try:
    # Call API
    response = requests.get(apiUrl + '/v1/status/wallet', headers=headers)
    # handle to success or fail
    print(response.status_code)
    print(response.json())
except Exception as err:
    # handle exception
    print(err)