# YouTube Caption Summaries

This Python tool retrieves the captions from a YouTube video, and then uses the OpenAI Chat API to summarize them.

## Prerequisites

- Python 3.8+
- An API key for the OpenAI Chat API
- A `config.yaml` file with your OpenAI Chat API key in the following format:

```yaml
openai:
  key: "your_openai_key"
```

## Installation

1. Clone this repository and navigate into it:

```bash
git clone https://github.com/your_username/yt-caption-summaries.git
cd yt-caption-summaries
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script with a YouTube video URL as follows:

```bash
python -m src.main "https://www.youtube.com/watch?v=jNQXAC9IVRw"
```

The summary of the video's captions will be saved in a `.txt` file in the `summaries` folder.

The tool tries to fetch English captions by default. If you want to specify another language for the original captions, you can do so with the `--lang` flag. For example, to fetch Swedish captions and then translate them into English:

```bash
python -m src.main "https://www.youtube.com/watch?v=AP-ocdDPRlk" --lang "sv"
```

## Contributing

Please feel free to fork this repository and submit pull requests. To install development dependencies, run `pip install -r requirements_dev.txt`.

## License

This project is licensed under the terms of the MIT license.
