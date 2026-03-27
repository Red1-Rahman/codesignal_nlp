import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from autocorrect import Speller
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords', quiet = True)
nltk.download('wordnet', quiet = True)

# Initialize spell checker and stopwords
spell = Speller(lang='en')
stop_words = set(stopwords.words('english'))

# Example text
text_sample = "Hello! Email me at example@mail.com. Visit https://example.com. Natural language processing is amzing! 😊"

# Remove URLs and emails
text_sample = re.sub(r'http\S+|www\S+|[\w.-]+@[\w.-]+', '', text_sample)
# Remove special characters, numbers, and punctuation
text_sample = re.sub(r'[^a-zA-Z\s]', '', text_sample)
# Normalize Unicode
text_sample = unicodedata.normalize("NFKC", text_sample)
# Convert to lowercase
text_sample = text_sample.lower()
# Remove stopwords and spell-check
words = text_sample.split()
words = [spell(word) for word in words if word not in stop_words]
text_sample = " ".join(words)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# TODO: Apply stemming to the words
stemmed_words = [stemmer.stem(word) for word in words]

# TODO: Apply lemmatization to the words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print results
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)