import argparse
from src.summarizer import summarize_video
import os

def main():
    parser = argparse.ArgumentParser(description="Summarize a YouTube video")
    parser.add_argument("url", help="The URL of the YouTube video")
    parser.add_argument("--lang", default='en', help="Original language of the video (defaults to English)")
    args = parser.parse_args()

    summary = summarize_video(args.url, args.lang)
    
    if summary:
        if not os.path.exists("summaries"):
            os.makedirs("summaries")

        with open(f'summaries/{args.url.split("v=")[-1]}.txt', 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"Summary saved to summaries/{args.url.split('v=')[-1]}.txt")
    else:
        print("Couldn't generate a summary for this video.")

if __name__ == "__main__":
    main()
