"""
Author: Ken Lambert

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

import random

# sentence = nounphrase verbphrase
def sentence():
    return nounphrase() + ' ' + verbphrase()

# nounphrase = article noun
def nounphrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

# verbphrase = verb nounphrase prepositionalphrase
def verbphrase():
    return random.choice(verbs) + ' ' + nounphrase() + ' ' + prepositionalphrase()

# prepositionalphrase = preposition nounphrase
def prepositionalphrase():
    return random.choice(prepositions) + ' ' + nounphrase()

def main(count = 1):
    """Runs the sentence generator once, ulness the caller
    provides an itneger argument greater than 1."""
    for x in range(count): print(sentence() + '\n')

if __name__ == '__main__':
    main(10)

                        


                        

