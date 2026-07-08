import requests
from tools.pdf_reader import summarize_pdf


class Nova:
    def __init__(self):
        self.current_document = None

    def chat(self, user_input):

        # 📄 PDF TOOL
        if user_input.startswith("pdf "):
            file_path = user_input.replace("pdf ", "").strip()

            document, summary = summarize_pdf(file_path)

            self.current_document = document

            return summary

        # 🧠 DOCUMENT MEMORY
        if self.current_document:

            prompt = f"""
You are NOVA.

The user has already loaded the following document.

-------------------------
{self.current_document}
-------------------------

Answer the user's question using ONLY the information in the document.

User's question:
{user_input}
"""

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.1",
                    "prompt": prompt,
                    "stream": False
                }
            )

            return response.json()["response"]

        # 💬 NORMAL CHAT
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1",
                "prompt": user_input,
                "stream": False
            }
        )

        return response.json()["response"]


def run_nova():
    nova = Nova()
    print("NOVA: Online (Ollama brain connected).")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("NOVA: Shutting down.")
            break

        response = nova.chat(user_input)
        print("\nNOVA:", response)


if __name__ == "__main__":
    run_nova()