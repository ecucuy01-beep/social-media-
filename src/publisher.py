import json
import os
import re
import sys
from dotenv import load_dotenv
from utils.discord_utils import DiscordClient
from utils.meta_utils import MetaClient

load_dotenv()

def resolve_env_vars(config):
      if isinstance(config, dict):
                return {k: resolve_env_vars(v) for k, v in config.items()}
elif isinstance(config, list):
        return [resolve_env_vars(i) for i in config]
elif isinstance(config, str):
        if config.isupper() or any(prefix in config for prefix in ["DISCORD", "FB", "IG", "META"]):
                      return os.environ.get(config, config)
                  return config

def parse_message_content(content):
      match = re.search(r"Client ID: `(.+?)`", content)
      client_id = match.group(1) if match else None
      caption = content.split("Client ID:")[0].replace("**DRAFT POST FOR", "").split("**")[1].strip() if "**" in content else content.split("Client ID:")[0].strip()
      if "**DRAFT POST FOR" in content:
                lines = content.split("\n")
                for i, line in enumerate(lines):
                              if i > 0 and line.strip() and "Client ID:" not in line:
                                                caption = "\n".join(lines[i:]).split("Client ID:")[0].strip()
                                                break
                                    return caption, client_id

        def main():
              config_path = "config.json"
              if not os.path.exists(config_path):import json
                import os
import re
import sys
from dotenv import load_dotenv
from utils.discord_utils import DiscordClient
from utils.meta_utils import MetaClient

load_dotenv()

def resolve_env_vars(config):
      if isinstance(config, dict):
                return {k: resolve_env_vars(v) for k, v in config.items()}
elif isinstance(config, list):
        return [resolve_env_vars(i) for i in config]
elif isinstance(config, str):
        if config.isupper() or any(prefix in config for prefix in ["DISCORD", "FB", "IG", "META"]):
                      return os.environ.get(config, config)
                  return config

def parse_message_content(content):
      match = re.search(r"Client ID: `(.+?)`", content)
    client_id = match.group(1) if match else None
    caption = content.split("Client ID:")[0].replace("**DRAFT POST FOR", "").split("**")[1].strip() if "**" in content else content.split("Client ID:")[0].strip()
    if "**DRAFT POST FOR" in content:
              lines = content.split("\n")
        for i, line in enumerate(lines):
                      if i > 0 and line.strip() and "Client ID:" not in line:
                                        caption = "\n".join(lines[i:]).split("Client ID:")[0].strip()
                                        break
                            return caption, client_id

def main():
      config_path = "config.json"
    if not os.path.exists(config_path):
              print(f"Error: {config_path} not found.")
        sys.exit(1)
    with open(config_path, "r") as f:
              raw_config = json.load(f)
    config = resolve_env_vars(raw_config)
    discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")
    meta_access_token = os.environ.get("META_ACCESS_TOKEN")
    if not discord_bot_token or not meta_access_token:
              print("Error: DISCORD_BOT_TOKEN or META_ACCESS_TOKEN not set.")
        sys.exit(1)
    discord = DiscordClient(discord_bot_token)
    meta = MetaClient(meta_access_token)
    companies_map = {c["client_id"]: c for c in config["companies"]}
    channel_ids = set()
    for company in config["companies"]:
              if "discord_channel_id" in company:
                            channel_ids.add(company["discord_channel_id"])
              elif "ENV_VAR" in company.get("discord_channel_id", ""):
            resolved_id = os.environ.get(company["discord_channel_id"])
            if resolved_id:
                              channel_ids.add(resolved_id)
                  for channel_id in channel_ids:
                            print(f"Polling channel {channel_id}...")
                            try:
                                          messages = discord.get_messages(channel_id, limit=20)
                                          for msg in messages:
                                                            msg_id = msg["id"]
                                                            content = msg["content"]
                                                            reactions = discord.get_reactions(channel_id, msg_id, "\u2705")
                                                            if reactions:
                                                                                  print(f"Message {msg_id} approved! Processing...")
                                                                                  caption, client_id = parse_message_content(content)
                                                                                  if not client_id or client_id not in companies_map:
                                                                                                            continue
                                                                                                        company = companies_map[client_id]
                                                                                  fb_page_id = company.get("fb_page_id")
                                                                                  ig_account_id = company.get("ig_account_id")
                                                                                  image_url = msg["attachments"][0]["url"] if msg.get("attachments") else None
                                                                                  if fb_page_id:
                                                                                                            meta.post_to_facebook(fb_page_id, caption, image_url)
                                                                                                        if ig_account_id and image_url:
                                                                                                                                  meta.post_to_instagram(ig_account_id, caption, image_url)
                                                                                                                              discord.delete_message(channel_id, msg_id)
                            except Exception as e:
                                          print(f"Error polling channel {channel_id}: {e}")
                              
                    if __name__ == "__main__":
                          main()print(f"Error: {config_path} not found.")
                        sys.exit(1)
                    with open(config_path, "r") as f:
                              raw_config = json.load(f)
                          config = resolve_env_vars(raw_config)
    discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")
    meta_access_token = os.environ.get("META_ACCESS_TOKEN")
    if not discord_bot_token or not meta_access_token:
              print("Error: DISCORD_BOT_TOKEN or META_ACCESS_TOKEN not set.")
        sys.exit(1)
    discord = DiscordClient(discord_bot_token)
    meta = MetaClient(meta_access_token)
    companies_map = {c["client_id"]: c for c in config["companies"]}
    channel_ids = set()
    for company in config["companies"]:
              if "discord_channel_id" in company:
                            channel_ids.add(company["discord_channel_id"])
elif "ENV_VAR" in company.get("discord_channel_id", ""):
            resolved_id = os.environ.get(company["discord_channel_id"])
            if resolved_id:
                              channel_ids.add(resolved_id)
                  for channel_id in channel_ids:
                            print(f"Polling channel {channel_id}...")
                            try:
                                          messages = discord.get_messages(channel_id, limit=20)
                                          for msg in messages:
                                                            msg_id = msg["id"]
                                                            content = msg["content"]
                                                            reactions = discord.get_reactions(channel_id, msg_id, "
