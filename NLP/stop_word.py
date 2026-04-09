import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

text="This is jsut some random things"
text=text.lower()
words=word_tokenize(text)
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in words if word not in stop_words]
print(f"Original Words: {words}")
print(f"After stop words removal:{filtered_words}")
 