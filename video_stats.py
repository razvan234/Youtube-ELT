import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

API_KEY = os.getenv('API_KEY')

channel_handle = 'MrBeast'

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}"

def get_channel_playlist_id( url):
    try:
        response = requests.get(url)
        data = response.json()
        channel_items = data['items'][0]
        return channel_items['contentDetails']['relatedPlaylists']['uploads']
    except requests.RequestException as e:
        raise e


playlist_id = get_channel_playlist_id(url)
print(playlist_id)

