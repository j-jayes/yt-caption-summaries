from src.youtube_api import get_video_id, get_transcript
from src.openai_api import summarize_text
from src.summarizer import summarize_video

url = 'https://www.youtube.com/watch?v=AP-ocdDPRlk'

# Test getting the video ID from the URL
video_id = get_video_id(url)
print(video_id)  # should output 'jNQXAC9IVRw'

# Test getting the transcript
transcript = get_transcript(video_id)
print(transcript[:500])  # print the first 500 characters of the transcript

# Test summarizing a part of the transcript
summary_part = summarize_text(transcript[:500])
print(summary_part)  # print the summary of the first 500 characters

# Test summarizing the entire video
summary = summarize_video(url)
print(summary)  # print the summary of the video
