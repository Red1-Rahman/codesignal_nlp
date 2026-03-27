import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from autocorrect import Speller
nltk.download('stopwords', quiet=True)

# Initialize spell checker and stopwords
spell = Speller(lang='en')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Normalize Unicode
    text = unicodedata.normalize("NFKC", text)
    # Convert to lowercase
    text = text.lower()
    # Remove URLs and emails
    text = re.sub(r'http\S+|www\S+|[\w.-]+@[\w.-]+', '', text)
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    
    # TODO: Split the text into words
    words = text.split()
    # TODO: Remove stopwords from the list of words and spell-check each word
    words = [spell(word) for word in words if word not in stop_words]
    # TODO: Join the words back into a single string
    text = ' '.join(words)

    return text
# Example text
text_sample = "Hello! Email me at example@mail.com. Visit https://example.com. Natural language processing is amzing! 😊"

# Print cleaned text
print("Cleaned Text:", clean_text(text_sample))