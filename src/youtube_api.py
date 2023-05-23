from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

def get_video_id(url):
    return url.split('v=')[-1]

def get_transcript(video_id, original_language='en'):
    try:
        # Get the list of all transcripts for the video
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Fetch the transcript in the original language
        transcript = transcript_list.find_transcript([original_language])

        # If the original language is not English, translate the transcript
        if original_language != 'en':
            transcript = transcript.translate('en')

        # Combine all segments into a single string
        return " ".join([seg['text'] for seg in transcript.fetch()])
    
    except Exception as e:
        print("An error occurred: ", str(e))
        return None
