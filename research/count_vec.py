## REFERENCE https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'apple ball cat man',
    'ball cat dog cat dog',
    'banana cat apple women',
    'dog cat'
]

max_features = 500   # no of words you want to consider
ngrams = 3  #pair of words you want to consider
vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())

print(X.toarray())