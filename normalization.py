import re

def clean_text(text):
    # Remove URLs and emails
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text, flags=re.MULTILINE)

    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^A-Za-z\s]', '', text)
    return text

# Example usage
text_sample = "Hello! Email me at example@mail.com. Visit https://example.com. Natural language processing is amzing! 😊"

cleaned_text = clean_text(text_sample)
print("Cleaned Text:", cleaned_text)