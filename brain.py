import requests


class Brain:
    """
    Handles all communication with the AI model (Ollama).
    """

    def __init__(self):
        self.model = "llama3.1"
        self.url = "http://localhost:11434/api/generate"

    def ask(self, prompt):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]