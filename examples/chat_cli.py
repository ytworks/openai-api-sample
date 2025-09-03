#!/usr/bin/env python3
"""
Simple CLI chat using the OpenAI Python client against a custom base URL.

Setup:
  1) Create a .env file (see .env.example) with OPENAI_API_KEY.
  2) Install deps: pip install -r requirements.txt
  3) Run: python examples/chat_cli.py
"""

import os
import sys
from typing import List, Dict

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    load_dotenv = None

try:
    from openai import OpenAI
except Exception as e:  # pragma: no cover
    print("OpenAI client is not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    raise


def getenv(name: str, default: str | None = None) -> str:
    val = os.environ.get(name)
    if val is None:
        if default is None:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return default
    return val


def main() -> int:
    # Load variables from .env if python-dotenv is available
    if load_dotenv is not None:
        load_dotenv()  # loads from .env if present

    api_key = getenv("OPENAI_API_KEY")
    base_url = getenv(
        "OPENAI_BASE_URL",
        "http://ip-61-206-39-8.aits-tyo-02.v4.digital-dynamic.co.jp:8000/v1/",
    )
    model = getenv("OPENAI_MODEL", "openai/gpt-oss-120b")

    client = OpenAI(api_key=api_key, base_url=base_url)

    # Maintain a short conversation history
    messages: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer concisely unless asked for detail.",
        }
    ]

    print("CLI connected.")
    print(f"Model: {model}")
    print("Type your message and press Enter. Ctrl+C to exit.\n")

    try:
        while True:
            try:
                user_input = input("You > ").strip()
            except EOFError:
                print()
                break

            if not user_input:
                continue

            # Support a simple command to reset state
            if user_input.lower() in {"/reset", ":reset"}:
                messages = messages[:1]  # keep only system prompt
                print("(conversation reset)")
                continue

            messages.append({"role": "user", "content": user_input})

            print("Assistant > ", end="", flush=True)
            acc = []

            try:
                stream = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    stream=True,
                )

                for chunk in stream:
                    delta = None
                    try:
                        delta = chunk.choices[0].delta.content  # type: ignore[attr-defined]
                    except Exception:
                        delta = None
                    if delta:
                        acc.append(delta)
                        print(delta, end="", flush=True)

                print()
            except KeyboardInterrupt:
                print("\n(cancelled)\n")
                # Remove the partial user message to avoid confusing history
                messages.pop()
                continue
            except Exception as e:
                print(f"\n[Error] {e}\n", file=sys.stderr)
                continue

            assistant_text = "".join(acc)
            messages.append({"role": "assistant", "content": assistant_text})

            # Trim history to avoid growing unbounded (keep last 10 turns + system)
            # A "turn" is one user+assistant pair -> keep ~21 messages total.
            if len(messages) > 21:
                # keep system + last 20
                messages = [messages[0]] + messages[-20:]

    except KeyboardInterrupt:
        print("\nBye!")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

