import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

API_KEY = os.getenv('API_KEY')

channel_handle = 'MrBeast'

maxResults = 50

def get_channel_playlist_id():
    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        channel_items = data['items'][0]
        return channel_items['contentDetails']['relatedPlaylists']['uploads']
    except requests.RequestException as e:
        raise e


def get_video_ids(playlistId):

    video_ids = []
    page_token = None

    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}"

    try:
        while True:
            url = base_url
            if page_token:
                url += f"&pageToken={page_token}"

            response = requests.get(url)
            data = response.json()

            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)
            
            page_token = data.get('nextPageToken')
            if not page_token:
                break
            
        return video_ids
    
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlistID = get_channel_playlist_id()
    video_ids = get_video_ids(playlistID)
