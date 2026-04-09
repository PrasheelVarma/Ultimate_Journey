from nltk.stem import PorterStemmer
porter_stemmer=PorterStemmer()
words=["running","roading","run","killing","kill","jumping","happiness"]
stemmed=[porter_stemmer.stem(word) for word in words]
print(f"original: {words}")
print(f"stemmed:{stemmed}")
