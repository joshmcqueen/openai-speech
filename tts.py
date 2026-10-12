import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


PROJECT_DIR = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn text into an MP3 with OpenAI's speech API."
    )
    parser.add_argument(
        "text",
        nargs="?",
        default="Today is a wonderful day to build something people love!",
        help="Text to speak.",
    )
    parser.add_argument(
        "--voice",
        default="coral",
        help="Built-in voice to use (default: coral).",
    )
    parser.add_argument(
        "--instructions",
        default="Speak in a warm, natural, conversational tone.",
        help="Directions for how the voice should speak.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_DIR / "speech.mp3",
        help="Where to save the MP3 (default: speech.mp3).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_dotenv(PROJECT_DIR / ".env")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            "Missing OPENAI_API_KEY. Copy .env.example to .env and add your key."
        )

    output_path = args.output.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    client = OpenAI()
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=args.voice,
        input=args.text,
        instructions=args.instructions,
        response_format="mp3",
    ) as response:
        response.stream_to_file(output_path)

    print(f"Saved AI-generated speech to {output_path}")


if __name__ == "__main__":
    main()
