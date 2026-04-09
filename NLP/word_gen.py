import string, random
words=8
word_length=5

for i in range(words):
    word="".join(random.choice(string.ascii_lowercase) for x in range(word_length))
    print(word)


    #wiat and
    for i in range(words):
        word="".join(random)