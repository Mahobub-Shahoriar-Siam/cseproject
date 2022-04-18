import nltk
from nltk.tag import pos_tag

def traverse(t):
  try:
      t.label()
  except AttributeError:
      return
  else:
      if t.label() == 'NP': print(t)  
      else:
          for child in t: 
              traverse(child)

def nounPhrase(tagged_sent):
    # Tag sentence for part of speech
    tagged_sent = pos_tag(sentence.split())  # List of tuples with [(Word, PartOfSpeech)]
    # Define several tag patterns
    grammar = r"""
      NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
      {<NN>+}                 # chunk consecutive nouns
      """
    cp = nltk.RegexpParser(grammar)  # Define Parser
    SentenceTree = cp.parse(tagged_sent)
    NounPhrases = traverse(SentenceTree)   # collect Noun Phrase
    return(NounPhrases)

def extract_np(psent):
  for subtree in psent.subtrees():
    if subtree.label() == 'NP':
      yield ' '.join(word for word, tag in subtree.leaves())
      
sentence =  input("Enter Text : ")

tagged_sent = pos_tag(sentence.split())
grammar = r"""
  
      NP: {<DT|PP\$>?<JJ>*<NN> and <(a|an|and|the)>}   # chunk determiner/possessive, adjectives and noun ,remove articale 
      {<NNP>+}                # chunk sequences of proper nouns
      {<NN>+}                 # chunk consecutive nouns
      """

cp = nltk.RegexpParser(grammar)
parsed_sent = cp.parse(tagged_sent)
for npstr in extract_np(parsed_sent):
    print (npstr)


#tagged_sent = pos_tag(sentence.split())  
#NP = nounPhrase(tagged_sent)  
#print(NP) 