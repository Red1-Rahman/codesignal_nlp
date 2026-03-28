from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Example Documents
docs = [
    "Machine learning and NLP are closely related fields. Machine learning is powerful.",
    "Bag-of-Words is a common technique in NLP. NLP is widely used.",
    "NLP models often use n-grams to improve performance. N-grams are useful."
]

# TODO: Modify the CountVectorizer to include unigrams and bigrams
vectorizer = CountVectorizer(ngram_range=(1,2), stop_words='english')
bow_matrix = vectorizer.fit_transform(docs)

# Convert to DataFrame for better visualization
df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print(df)