import requests

# Authentication credentials
client_id = '821518b576c74854859c9727052bdb6b'
client_secret = 'e124007031b6485697ef98bee56590cc'

# Base URL for Spotify token endpoint
token_endpoint = 'https://accounts.spotify.com/api/token'

# Request body parameters
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

# Headers for the request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Send the POST request to the token endpoint
response = requests.post(token_endpoint, data=data, headers=headers)

# Check if request was successful
if response.ok:
    # Parse the JSON response
    response_data = response.json()
    # Extract and print the access token
    access_token = response_data.get('access_token')
    print('Access Token:', access_token)   
else:
    print('Error:', response.text)



# access_token: BQA9XKOeOwIWgyoGzjlrxgl-RTZzNCr_t5zJQm6NbyvNfWgdGN4k5AyB52GBHD_3UzXxPh3FOwT6KGlWInAzAuRSwHbmpcTly1PI1lzTuSryXdsoWoQ
    
# curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \
#      -H "Authorization: Bearer  BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"




