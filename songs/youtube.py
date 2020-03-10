import html

from apiclient.discovery import build

import settings

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
VIDEO_TYPE = 'video'
client = build(API_SERVICE_NAME, API_VERSION, developerKey=settings.DEVELOPER_KEY)


def search(query, max_result=settings.RESULTS_COUNT):
    results = client.search().list(q=query, type=VIDEO_TYPE, part="id", maxResults=max_result).execute()
    return results.get('items', [])


def fetch_video_details(query, video_ids):
    video_details = client.videos().list(id=video_ids, part="snippet, contentDetails").execute()
    results = video_details.get("items", [])
    videos = [f'**{query.title()}**\n\n']
    counter = 1
    for result in results:
        title = html.unescape(result["snippet"]["title"])
        duration = convert_iso_time_format(result["contentDetails"]["duration"])
        videos.append(f'`{counter}.` {title} **[{duration}]**')
        counter += 1
    return '\n'.join(videos)


def list_videos(query):
    video_ids = ', '.join([result["id"]["videoId"] for result in search(query)])
    return fetch_video_details(query, video_ids)


def convert_iso_time_format(timestamp):
    timestamp = timestamp[2:]
    minutes, seconds = timestamp.split('M')
    return f'{minutes}:{seconds.split("S")[0]}'
