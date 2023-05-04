#!/usr/bin/env python3

import argparse
import os
import requests

def generate_response(api_key, prompt):
    model = "text-davinci-003"
    max_tokens = 4000
    temperature = 1.0

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    response_text = result["choices"][0]["text"].strip()

    return response_text

def main():
    parser = argparse.ArgumentParser(description="Generate text using OpenAI's GPT-3 API.")
    parser.add_argument("prompt", help="The prompt to generate text from.")
    args = parser.parse_args()

    api_key = input("Please enter your OpenAI API key: ")
    response_text = generate_response(api_key, args.prompt)

    print(f"Input Prompt: {args.prompt}")
    print(f"Response: {response_text}")

if __name__ == "__main__":
    main()
