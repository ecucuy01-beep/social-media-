import base64
import os
from google import genai
from google.genai import types

class GeminiClient:
      def __init__(self, api_key: str):
                self.client = genai.Client(api_key=api_key)
                self.text_model = "gemini-3.1-pro-preview"
                self.image_model = "gemini-3.1-flash-image-preview"

      def generate_caption(self, name: str, focus_areas: list, keywords: list) -> str:
                prompt = f"""
                        Generate a professional and engaging social media caption for {name}.
                                Focus areas: {', '.join(focus_areas)}
                                        Keywords: {', '.join(keywords)}
                                                The caption should be informative, include a call to action with the company's contact info if provided, and use relevant hashtags.
                                                        Keep it under 2000 characters.
                                                                """
                response = self.client.models.generate_content(
                    model=self.text_model,
                    contents=prompt
                )
                return response.text.strip()

      def generate_social_image(self, name: str, focus_areas: list, keywords: list) -> str:
                """
                        Generates an image and returns the base64 encoded data or saves it to a temporary file.
                                For this implementation, we'll save it to a local 'temp_images' folder.
                                        """
                prompt = f"Professional social media marketing image for an insurance agency named {name}. Theme: {' and '.join(focus_areas)}. Style: Clean, modern, high quality, professional photography."

        # Using the new Imagen 3 capability via google-genai
                response = self.client.models.generate_images(
                    model=self.image_model,
                    prompt=prompt,
                    config=types.GenerateImageConfig(
                        number_of_images=1,
                        include_rai_reasoning=True,
                        output_mime_type="image/jpeg"
                    )
                )

        # The output is a list of generated images
                image_data = response.generated_images[0].image_bytes

        # Save to a temporary file for the generator to pick up
                os.makedirs("temp_images", exist_ok=True)
                filename = f"temp_images/{name.replace(' ', '_').lower()}.jpg"
                with open(filename, "wb") as f:
                              f.write(image_data)

                return filename
