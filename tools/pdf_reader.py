from pypdf import PdfReader
import requests


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def summarize_pdf(file_path):
    text = read_pdf(file_path)

    if not text.strip():
        return None, "No readable text found."

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": f"Summarize this document clearly:\n\n{text}",
            "stream": False
        }
    )

    summary = response.json()["response"]

    return text, summary