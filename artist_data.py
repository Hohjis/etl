import json
import requests

access_token = 'BQBGNrHzs0zu2WHr86kow--BUj5P3m9kG2PKR_w8EYsFAjPeFY_wgej3pL7a6CNym3qNPtL-6B3Oz2J2lY23n38tCzgT5wu2DnHBEQ3801t4kHLEWtE'

base_url = 'https://api.spotify.com/v1'

artists_id = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'

endpoint = f'/artists?ids={artists_id}'

# Headers for the request
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(base_url + endpoint, headers=headers)

if response.ok:
    # Parse the JSON response
    artist_data = response.json()
    print(json.dumps(artist_data, indent=4))
else:
    print('Error:', response.text)
