from nltk.tokenize import sent_tokenize

points = 0

text = """Kids were laughing in my classes, while I was scheming for the masses. Who do you think you are? 
Dreaming 'bout being a big star."""

tokenized_text=sent_tokenize(text)
#split up sentences

print(tokenized_text)s