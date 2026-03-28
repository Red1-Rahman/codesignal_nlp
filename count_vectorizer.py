from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Example Documents
docs = [
    "Machine learning and NLP are closely related fields. Machine learning is powerful.",
    "Bag-of-Words is a common technique in NLP. NLP is widely used.",
    "NLP models often use n-grams to improve performance. N-grams are useful."
]

# TODO: Initialize CountVectorizer with n-gram range for unigrams only
vectorizer = CountVectorizer(ngram_range=(1, 1))

# Fit vectorizer first, then read vocabulary/features
doc_term_matrix = vectorizer.fit_transform(docs)
print("Vocabulary:", vectorizer.get_feature_names_out())

# TODO: Convert to DataFrame for better visualization
df = pd.DataFrame(doc_term_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print(df)