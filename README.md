# OpenAI text to speech

A minimal Python example that saves AI-generated speech as an MP3.

## Setup

1. Open `.env` and add your OpenAI API key:

   ```dotenv
   OPENAI_API_KEY=your_api_key_here
   ```

2. Install the dependencies:

   ```bash
   uv sync
   ```

3. Generate speech:

   ```bash
   uv run python tts.py "Hello! This is my first text-to-speech test."
   ```

The result is saved to `speech.mp3`. You can also customize the voice, speaking
style, and output path:

```bash
uv run python tts.py "Welcome to the show." \
  --voice marin \
  --instructions "Speak slowly and confidently." \
  --output welcome.mp3
```

OpenAI requires you to clearly disclose to listeners that the voice is
AI-generated rather than human.
