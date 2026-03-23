import requests
import time

class MetaClient:
    def __init__(self, access_token: str):
            self.access_token = access_token
                    self.base_url = "https://graph.facebook.com/v19.0"

                        def post_to_facebook(self, page_id: str, message: str, image_url: str = None):
                                """Posts to a Facebook Page feed."""
                                        url = f"{self.base_url}/{page_id}/photos" if image_url else f"{self.base_url}/{page_id}/feed"
                                                params = {
                                                            "access_token": self.access_token,
                                                                        "message": message
                                                                                }
                                                                                        if image_url:
                                                                                                    params["url"] = image_url
                                                                                                                
                                                                                                                        response = requests.post(url, params=params)
                                                                                                                                response.raise_for_status()
                                                                                                                                        return response.json()
                                                                                                                                        
                                                                                                                                            def post_to_instagram(self, ig_account_id: str, caption: str, image_url: str):
                                                                                                                                                    """Posts to an Instagram Professional account."""
                                                                                                                                                            # Step 1: Create media container
                                                                                                                                                                    url_media = f"{self.base_url}/{ig_account_id}/media"
                                                                                                                                                                            params_media = {
                                                                                                                                                                                        "access_token": self.access_token,
                                                                                                                                                                                                    "image_url": image_url,
                                                                                                                                                                                                                "caption": caption
                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                response_media = requests.post(url_media, params=params_media)
                                                                                                                                                                                                                                        response_media.raise_for_status()
                                                                                                                                                                                                                                                creation_id = response_media.json().get("id")
                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                # Step 2: Check status of container (optional but safe)
                                                                                                                                                                                                                                                                        # In a real app, you'd poll /creation_id?fields=status_code
                                                                                                                                                                                                                                                                                # For simplicity, we'll wait a few seconds
                                                                                                                                                                                                                                                                                        time.sleep(5)
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                        # Step 3: Publish media
                                                                                                                                                                                                                                                                                                                url_publish = f"{self.base_url}/{ig_account_id}/media_publish"
                                                                                                                                                                                                                                                                                                                        params_publish = {
                                                                                                                                                                                                                                                                                                                                    "access_token": self.access_token,
                                                                                                                                                                                                                                                                                                                                                "creation_id": creation_id
                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                response_publish = requests.post(url_publish, params=params_publish)
                                                                                                                                                                                                                                                                                                                                                                        response_publish.raise_for_status()
                                                                                                                                                                                                                                                                                                                                                                                return response_publish.json()
