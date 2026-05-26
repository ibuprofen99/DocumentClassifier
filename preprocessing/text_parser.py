# read text from file
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def clean_text(text):
    text = text.lower()
    text = text.strip()
    cleaned = ""
    for char in text:
        if char.isalpha() or char == " ":
            cleaned += char
    cleaned = " ".join(cleaned.split())
    return cleaned
