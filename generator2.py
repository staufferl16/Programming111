"""
Author: Leigh Stauffer
Project Number: 5-1
File Name: generator2.py

This module defines a grammar and a vocabulary for generating random sentences

To generate several sentences, call main(<an int>)

To generate a single sentence, call sentence()

"""

nouns = ['bat', 'boy', 'girl', 'dog', 'cat', 'chair',
         'fence', 'table', 'computer', 'cake', 'field']

verbs = ['hit', 'threw', 'pushed', 'ate', 'dragged', 'jumped']

prepositions = ['with', 'to', 'from', 'on', 'below',
                'above', 'beside']

articles = ['a', 'the']

adjectives = ['heavy', 'strange', 'large', 'red', 'blue', 'silly', 'angsty']

conjunctions = [', and', ', but'] 

import random

# sentence = nounphrase verbphrase 
def sentence():
    probClause = random.randint(1,2)
    if probClause == 1:
        return nounphrase() + ' ' + verbphrase()
    else:
        return nounphrase() + ' ' + verbphrase() + ' ' + random.choice(conjunctions) + ' ' + nounphrase() + ' ' + verbphrase()
    
# nounphrase = article noun
def nounphrase():
    probAdj = random.randint(1,3)
    if probAdj == 1:
        return random.choice(articles) + ' ' + random.choice(nouns)
    else:
        return random.choice(articles) + ' ' + random.choice(adjectives) + ' ' + random.choice(nouns)

# verbphrase = verb nounphrase prepositionalphrase
def verbphrase():
    probPrep = random.randint(0,2)
    if probPrep == 0:
        return random.choice(verbs) + ' ' + nounphrase() + ' ' + prepositionalphrase()
    else:
        return random.choice(verbs) + ' ' + nounphrase()
    
# prepositionalphrase = preposition nounphrase
def prepositionalphrase():
    return random.choice(prepositions) + ' ' + nounphrase()
        
# defining main(n) 
def main(count = 1):
    """Runs the sentence generator once, ulness the caller
    provides an itneger argument greater than 1."""
    for x in range(count): print(sentence() + '\n')

if __name__ == '__main__':
    main(10)

                        


                        

