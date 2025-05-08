from google import genai
client = genai.Client(api_key="AIzaSyD8_G1Wc9h8n1R382lCiQnInP_yckCLsjM")

class GPTService:
    def __init__(self, model: str = "gemini-2.0-flash"):
        self.model = model

    def chat(self, system_prompt, user_prompt) -> str:
        response = client.models.generate_content(
            model=self.model,
            contents=user_prompt
        )
        return response.text