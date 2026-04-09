print("Tokenizing Manually")
print(len("Welcome to my world")) #the sentence with it's length
s=["Welcome","to","my","world"] #manual tokenization (splitting)
print(s)
print(len(s)) 
sorted_s=sorted(s)
print(sorted_s)
combined=s+sorted_s
print(combined)
print("\n")
#--------------------------------------------------------------------------------------
print("The official way of this tokenization")
text="Remember the day, This is the day you almost caught -Captain Jack Sparrow"
tokens=text.split()
print(f"The text:{text}")
print(f"The length of text:{len(text)}")
print(f"The generated token:{tokens}")
print(f"The length of the token:{len(tokens)}")
print(f"sorting the token:{sorted(tokens)}")
print("\n")
#--------------------------------------------------------------------------------------
print("The tokenization using NLTK")
import nltk
# Run this once to download the required logic
nltk.download('punkt_tab')

text = "Welcome to my world! It's amazing."

# Method A: Basic Python
split_tokens = text.split()

# Method B: NLTK (The AI/ML standard)
nltk_tokens = nltk.word_tokenize(text)

print(f"Original Text: {text}")
print(f"Basic Split: {split_tokens}") #split() function
print(f"NLTK Tokens: {nltk_tokens}") #word_tokenize

