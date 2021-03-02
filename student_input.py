#using NLTK library, we can do lot of text preprocesing
import nltk
import ssl

#try:
#    _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
#    pass
#else:
#    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#function to split text into word

stop_words = set(stopwords.words("english"))
#print(stop_words)
tokens = word_tokenize("The quick brown fox jumps over the lazy dog")

word_list = ["quick","brown","fox","jump","over","lazy"]
print(tokens)

filtered_sentence = []
word_values = []

place = -1
for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        place = place + 1
        for i in range(len(word_list)):
            print(i, "place =", place)
            print(word_list[i])
            if w == word_list[i]:
                print("found work",i)
                word_values.append(i)

print(word_values)
print(filtered_sentence)
