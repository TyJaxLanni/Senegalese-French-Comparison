import nltk, re

import nltk.data
#chargement du tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')

from nltk.stem.snowball import FrenchStemmer #import the French stemming library

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


# Loading the data 
#words = [w.lower() for w in ]

def stem_words(words):
    '''stems the word list using the French Stemmer'''
    #stemming words
    stemmed_words = [] #declare an empty list to hold our stemmed words
    stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
    for word in words:
        stemmed_word=stemmer.stem(word) #stem the word
        stemmed_words.append(stemmed_word) #add it to our stemmed word list
    stemmed_words.sort() #sort the stemmed_words
    return stemmed_words


tokens = []
with open("corpus_cleaned.txt", "r") as corpus:
	for line in corpus:
		line = line.strip()
		line_tokens = nltk.tokenize.word_tokenize(line)
		#line = re.sub("[^-9A-Za-z ]", "" , line)
		
		#for word in line.split():
		#line_tokens = nltk.wordpunct_tokenize(line)
		for tok in line_tokens:
			tokens.append(tok)

		

	biagram_collocation = BigramCollocationFinder.from_words(tokens)
	#biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 15)

	print(biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 15))



#with open("corpus_cleaned.txt", "r") as corpus:
#	tokens = dict()
#	count = 0
#	word_count = 0
#	for line in corpus:
#		if count > 100:
#			break
#
#		else:
#			for word in line.split():
#				#print(word.lower())
#				word_count += 1
#				token = word.lower()
#				if token in tokens.keys():
#					tokens[token] += 1
#				else:
#					tokens[token] = 1
#
#		count += 1
#
#	#print(tokens.values())
#	print(word_count)

