"""
Author: Ken Lambert

This program simulates a session of non-directive psychotherapy.
The program (doctor) prints a greeting and waits for the user
(patient) to answer an initial question.  Each answer entered
by the user results in a related reply by the program that
continues the conversation.  When the user enters 'quit,' the
program signs off with a goodbye.
"""

# Data structures for the program
# These are usually defined early in a module

qualifiers = ['Why do you say that ', 'You seem to think that ',
              'Did I just hear you say that ']

replacements = {'I':'you', 'me':'you', 'my':'your',
                'we':'you', 'us':'you'}

# imports and function definitions
# Note how the functions collaborate to solve the problem

import random

def main():
    """
    Main driver loop for the program.  Takes user's inputs
    and prints replies until the user enters quit.
    """
    print('Good morning, how can I help you today?')
    while True:
        sentence = input('> ')
        if sentence.upper() == 'QUIT':
            break
        print(reply(sentence))
    print('Have a nice day!')

def reply(sentence):
    """
    Generates and returns replies to user's sentences.
    The current option is to change persons and prepend
    an interrogatory qualifier.
    """
    return random.choice(qualifiers) + \
           change_person(sentence)

def change_person(sentence):
    """
    Returns a string representing the argument sentence
    with the personal pronouns transformed.
    """
    oldlist = sentence.split()
    newlist = []
    for word in oldlist:
        newlist.append(replacements.get(word, word))
    return ' '.join(newlist)

if __name__ == "__main__":
    main()           
            
    

    
        
    



    
    
    

