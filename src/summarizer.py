from .youtube_api import get_transcript, get_video_id
from .openai_api import summarize_text

def summarize_video(url):
    video_id = get_video_id(url)
    transcript = get_transcript(video_id)
    
    summary = ""
    for i in range(0, len(transcript), 2048):
        batch = transcript[i:i+2048]
        summary += summarize_text(batch)
    
    return summary
