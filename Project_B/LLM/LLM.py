import requests
import time
import sys
from dotenv import load_dotenv
import os


load_dotenv()
BASE_URL = os.getenv('BASE_URL', '')
API_KEY = os.getenv('API_KEY')



headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY,
}


data_file = "data_file.txt"
def save_chat(user_prompt, text):
    with open(data_file, 'a', encoding='utf-8') as file:
        file.write(f"You:{user_prompt}\nGemini: {text}\n\n")


system_prompt = "You are an AI lawyer specializing in Indian cyber laws. Always respond in simple terms. If you got anything else rather indian cyber '''say sorry i can help you with Indian Cyber Law''' "


def typing_effect(text):
    for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.005)
    print()


def main():
    print("Ask Gemini anything: \n")
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() in ['exit', 'quit']:
            print("Goodbye!!")
            break
        
        full_prompt = f"System Prompt:{system_prompt}\n User Prompt:{user_prompt}"

        data = {
            "contents": [
                {
                    "parts": [{"text": full_prompt}]
                }
            ]
        }

        try:
            response = requests.post(BASE_URL, headers=headers, json=data, timeout=20)
            response.raise_for_status()
            result = response.json()
            print("\n🤖 Gemini says:\n")
            text= result['candidates'][0]['content']['parts'][0]['text']

            typing_effect(text)
            save_chat(user_prompt, text)

        except requests.exceptions.RequestException as e:
            print("Error",e)


if __name__ == "__main__":
    main()
