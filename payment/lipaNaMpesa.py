import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth


import mpesaKeys

unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d")
print(formatted_time)


# data_to_encode = mpesaKeys.business_short_code + mpesaKeys.lipa_na_mpesa_passkey + formatted_time
# encoded_string = base64.b64encode(data_to_encode.encode())
# decoded_password = encoded_string.decode('utf-8')
# print(decoded_password)


consumer_key = mpesaKeys.consumer_key
consumer_secret = mpesaKeys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))


json_response = r.json()
my_access_token = json_response['access_token']


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": mpesaKeys.business_short_code,
        "Password": mpesaKeys.password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": mpesaKeys.phone_number,
        "PartyB": mpesaKeys.business_short_code,
        "PhoneNumber": mpesaKeys.phone_number,
        "CallBackURL": "https://ip_address:port/callback",
        "AccountReference": " ",
        "TransactionDesc": " "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
    
lipa_na_mpesa()