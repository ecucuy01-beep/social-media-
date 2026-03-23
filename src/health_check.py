import os
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

def check_gemini():
      print("Checking Gemini API...")
      try:
                client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
                models = client.models.list()
                print("\u2705 Gemini API Key is valid.")
except Exception as e:
        print(f"\u274c Gemini API Error: {e}")

def check_discord():
      print("Checking Discord Bot Token...")
      token = os.environ.get("DISCORD_BOT_TOKEN")
      headers = {"Authorization": f"Bot {token}"}
      try:
                response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
                if response.status_code == 200:
                              print(f"\u2705 Discord Bot Token is valid (User: {response.json()['username']})")
      else:
                    print(f"\u274c Discord API Error: {response.status_code} - {response.text}")
except Exception as e:
        print(f"\u274c Discord Error: {e}")

def check_meta():
      print("Checking Meta Access Token...")
      token = os.environ.get("META_ACCESS_TOKEN")
      try:
                response = requests.get(f"https://graph.facebook.com/v19.0/me?access_token={token}")
                if response.status_code == 200:
                              print(f"\u2705 Meta Access Token is valid (User ID: {response.json().get('id')})")
      else:
                    print(f"\u274c Meta API Error: {response.status_code} - {response.text}")
except Exception as e:
        print(f"\u274c Meta Error: {e}")

if __name__ == "__main__":
      check_gemini()
      check_discord()
      check_meta()
