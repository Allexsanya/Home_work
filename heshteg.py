import string

text = "let's do it 123"
text = ''.join(char for char in text if char not in string.punctuation)
words = text.split()
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())
hashtag = '#' + ''.join(capitalized_words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)