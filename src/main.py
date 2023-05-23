import os
import argparse
from .summarizer import summarize_video

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='The URL of the YouTube video to summarize')
    args = parser.parse_args()

    summary = summarize_video(args.url)

    if not os.path.exists('summaries'):
        os.makedirs('summaries')

    video_id = args.url.split('v=')[-1]
    with open(f'summaries/{video_id}.txt', 'w') as f:
        f.write(summary)

if __name__ == '__main__':
    main()
