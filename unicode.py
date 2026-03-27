import re
import unicodedata

# Example text
text_sample = "Hello! Email me at example@mail.com. Visit https://example.com. Natural language processing is amzing! 😊"

def clean_text(text):
    # Remove URLs and emails
    text = re.sub(r'http\S+|www\S+|[\w.-]+@[\w.-]+', '', text)
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # TODO: Convert to lowercase
    text = text.lower() 
    # TODO: Normalize Unicode
    text = unicodedata.normalize('NFKD', text)

    return text

# Clean the text using the function
cleaned_text = clean_text(text_sample)

# Print cleaned text
print("Cleaned Text:", cleaned_text)