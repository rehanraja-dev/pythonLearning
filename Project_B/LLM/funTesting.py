import requests
import time
import sys
from colorama import Fore, Style

# Gemini API details
API_KEY = "AIzaSyCK8PINqeK8WhvZR6LDvU8Hljyy55DmzAA"
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "Tell me a short motivational quote"}
            ]
        }
    ]
}

print(Fore.YELLOW + "\n🤖 Asking Gemini...\n")
response = requests.post(URL, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    text = result['candidates'][0]['content']['parts'][0]['text']

    print(Fore.CYAN + "Gemini says:\n")
    for char in text:
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()
        time.sleep(0.04)  # ⏱️ Adjust typing speed here (0.04 = fast, 0.1 = slower)
    print(Style.RESET_ALL + "\n\n✅ Done!\n")

else:
    print(Fore.RED + f"Error {response.status_code}: {response.text}")
