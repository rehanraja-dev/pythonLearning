import requests
import time
import sys
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()
BASE_URL = os.getenv('BASE_URL')
API_KEY = os.getenv('API_KEY')

# Validate environment variables
if not BASE_URL or not API_KEY:
    print("❌ Error: BASE_URL and API_KEY must be set in .env file")
    sys.exit(1)

# HTTP headers for API requests
headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY
}

# File to store chat history
DATA_FILE = "data_file_copied_version.txt"

# System prompt defining the AI's role
SYSTEM_PROMPT = """You are an AI lawyer specializing in Indian cyber laws including:
- Information Technology Act, 2000 (IT Act)
- Digital Personal Data Protection Act, 2023
- Indian Penal Code provisions related to cyber crimes
- IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021

Always respond in simple, easy-to-understand terms. Provide practical advice while 
reminding users to consult a qualified lawyer for specific legal matters."""


def save_chat(user_message, assistant_response):
    """
    Save conversation to a text file with timestamp.
    
    Args:
        user_message: The user's question
        assistant_response: Gemini's response
    """
    try:
        with open(DATA_FILE, 'a', encoding='utf-8') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}]\n")
            file.write(f"You: {user_message}\n")
            file.write(f"Gemini: {assistant_response}\n")
            file.write("-" * 80 + "\n\n")
    except IOError as e:
        print(f"\n⚠️  Warning: Could not save chat history: {e}")


def typing_effect(text, delay=0.005):
    """
    Display text with a typing effect.
    
    Args:
        text: The text to display
        delay: Delay between characters in seconds
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end


def send_to_gemini(user_prompt):
    """
    Send a message to Gemini API and return the response.
    
    Args:
        user_prompt: The user's question
        
    Returns:
        tuple: (success: bool, response_text: str or error_message: str)
    """
    # Combine system prompt with user prompt
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_prompt}"
    
    # Prepare API payload
    data = {
        "contents": [
            {
                "parts": [{"text": full_prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 2048,
        }
    }
    
    try:
        # Make API request
        response = requests.post(BASE_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        
        # Extract text from response
        if 'candidates' in result and len(result['candidates']) > 0:
            text = result['candidates'][0]['content']['parts'][0]['text']
            return True, text
        else:
            return False, "Unexpected API response format"
            
    except requests.exceptions.Timeout:
        return False, "Request timed out. Please check your internet connection and try again."
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return False, "Authentication failed. Please check your API key."
        elif response.status_code == 429:
            return False, "Rate limit exceeded. Please wait a moment and try again."
        elif response.status_code == 400:
            return False, "Bad request. The prompt may contain invalid content."
        else:
            return False, f"HTTP Error {response.status_code}: {str(e)}"
            
    except requests.exceptions.ConnectionError:
        return False, "Connection failed. Please check your internet connection."
        
    except requests.exceptions.RequestException as e:
        return False, f"Request error: {str(e)}"
        
    except (KeyError, IndexError) as e:
        return False, f"Error parsing API response: {str(e)}"
        
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def display_welcome():
    """Display welcome message and instructions."""
    print("=" * 80)
    print("⚖️  INDIAN CYBER LAW AI ASSISTANT")
    print("=" * 80)
    print(f"\nSpecializing in:")
    print("  • Information Technology Act, 2000")
    print("  • Digital Personal Data Protection Act, 2023")
    print("  • Cyber crime provisions under IPC")
    print("  • Digital media and intermediary regulations")
    print(f"\n💡 Tip: Responses are saved to '{DATA_FILE}' for your reference")
    print(f"\n📝 Commands: Type 'exit' or 'quit' to end the conversation")
    print("=" * 80)
    print("\nAsk your cyber law question:\n")


def main():
    """Main chat loop."""
    display_welcome()
    
    conversation_count = 0
    
    while True:
        try:
            # Get user input
            user_prompt = input("You: ").strip()
            
            # Check for empty input
            if not user_prompt:
                print("⚠️  Please enter a question.\n")
                continue
            
            # Check for exit commands
            if user_prompt.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                print(f"\n👋 Goodbye! You asked {conversation_count} question(s) today.")
                print(f"📁 Your chat history is saved in '{DATA_FILE}'\n")
                break
            
            # Send request to Gemini
            print("\n🤖 Gemini (Indian Cyber Law Expert):\n")
            success, response = send_to_gemini(user_prompt)
            
            if success:
                # Display with typing effect
                typing_effect(response)
                
                # Save to file
                save_chat(user_prompt, response)
                conversation_count += 1
            else:
                # Display error message
                print(f"❌ Error: {response}")
            
            print()  # Extra line for spacing
            
        except KeyboardInterrupt:
            print(f"\n\n👋 Interrupted! You asked {conversation_count} question(s).")
            print(f"📁 Your chat history is saved in '{DATA_FILE}'\n")
            break
            
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()