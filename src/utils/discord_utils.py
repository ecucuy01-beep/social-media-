import requests
  import json
  import os

  class DiscordClient:
      def __init__(self, bot_token: str = None):
        self.bot_token = bot_token
                  self.base_url = "https://discord.com/api/v10"
                  self.headers = {
                      "Authorization": f"Bot {self.bot_token}",
                      "Content-Type": "application/json"
        } if bot_token else {}

    def send_via_webhook(self, webhook_url: str, content: str, image_path: str = None):
        """Sends a message with an optional image via Webhook (Phase 1)"""
                  data = {"content": content}
        files = {}

        if image_path and os.path.exists(image_path):
            files = {"file": open(image_path, "rb")}

        response = requests.post(webhook_url, data={"payload_json": json.dumps(data)}, files=files)
                  response.raise_for_status()
                  return response.json()

              def get_messages(self, channel_id: str, limit: int = 10):
        """Polls messages from a channel (Phase 3)"""
                  url = f"{self.base_url}/channels/{channel_id}/messages?limit={limit}"
                  response = requests.get(url, headers=self.headers)
                  response.raise_for_status()
                  return response.json()

              def delete_message(self, channel_id: str, message_id: str):
        """Deletes a message from a channel (Phase 3)"""
                  url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}"
                  response = requests.delete(url, headers=self.headers)
                  response.raise_for_status()

              def get_reactions(self, channel_id: str, message_id: str, emoji: str = "check"):
        """Checks for specific reactions on a message (Phase 3)"""
                  # Encode emoji for URL
                  encoded_emoji = requests.utils.quote(emoji)
                  url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}/reactions/{encoded_emoji}"
                  response = requests.get(url, headers=self.headers)
                  response.raise_for_status()
                  return response.json() # Returns list of users who reacted
