from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from .config import config

YOUTUBE_API_KEY = config["youtube"]["key"]

def get_video_id(url):
    return url.split('v=')[-1]

def get_transcript(video_id):
    try:
        # Try to get the transcript in any available language
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = None

        # Try to fetch the English transcript (auto-generated or not)
        try:
            transcript = transcript_list.find_transcript(['en'])
        except NoTranscriptFound:
            pass

        # If English transcript is not found, fetch the first available transcript
        if not transcript:
            transcript = transcript_list.find_transcript(transcript_list.get_language_list())
        
        return " ".join([seg['text'] for seg in transcript.fetch()])
    
    except Exception as e:
        print("An error occurred: ", str(e))
        return None