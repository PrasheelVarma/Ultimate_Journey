##Program 1a
#to tokenize a sentence for tomorrow exam
text=("This is a text")
#now tolenize it
tokens= text.split()
#the results
print(f"The text we taken:{text}")
print(f"the length of this text:{len(text)}")
print(f"The text after tokenized:{tokens}")
print(f"The length of this tokens now:{len(tokens)}")
#additional things to do
print(f"let's add the text we taken and the tokens that we tokenized for this text:{text}{tokens}")
print(f"Let's sort the words that we tokenized in the text:{sorted(tokens)}")

##Program 1b
#to implement this stop words
import nltk
from nltk.tokenize import word_tokenize #(same like that split() but used as a nlp)
from nltk.corpus import stopwords
text="This is  text for implementing this fucking STOP WORDS by using NLTK".lower()
print(f"This are the words initially taken{text}")
#lets tokenize
text=word_tokenize(text)
#lets begin removal of stop words
stop_words=set(stopwords.words('english'))
f_words=[word for word in words if word not in stop_words]
print(f"After removing the top words this are words:{f_words}")

#the program 2
print("Porter Stemmer for stemming")
from nltk.stem import PorterStemmer
ps=PorterStemmer()
words=["running","jumps","happily"]
print(f"the words:{words}")
sw=[ps.stem(word) for word in words]
print(f"the stemmed words:{sw}")



