import nltk
text = "The passing rate of science group under the general education boards is 94.16%vb  "

sent  =  nltk.sent_tokenize(text)


loftags = []
for s in sent:
    d = nltk.word_tokenize(s)   

    print(nltk.pos_tag(d)) 