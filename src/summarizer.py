from .youtube_api import get_transcript, get_video_id
from .openai_api import summarize_text

def summarize_video(url, original_language='en'):
    video_id = get_video_id(url)
    transcript = get_transcript(video_id, original_language)
    
    summary = ""
    if transcript:
        for i in range(0, len(transcript) if transcript else 0, 2048):
            batch = transcript[i:i+2048]
            if batch:
                summary += summarize_text(batch) or ""
    
    return summary
