"""
Author: Leigh Stauffer
Project Number: 5-2
File Name: doctor2.py

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

replacements = {'i':'you', 'me':'you', 'my':'your',
                'we':'you', 'us':'you', 'you':'i', 'am':'are'}

hedges = ['Please, tell me more...', 'That is interesting. Please, elaborate...', 'Please, go on...']

references = ['Earlier you said that ']

patientHistory = []

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
        else:
            sentence = sentence.lower()
            patientHistory.append(sentence)
        print(reply(sentence))
    print('Have a nice day!')

def reply(sentence):
    """
    Generates and returns replies to user's sentences.
    The current option is to change persons and prepend
    an interrogatory qualifier.
    """
    probReply = random.randint (1,3)
    if probReply == 1:
        return random.choice(qualifiers) + \
           change_person(sentence)
    elif probReply == 2:
        return random.choice(hedges)
    elif probReply == 3 and len(patientHistory) >= 3:
        return "Earlier you said that " + change_person(random.choice(patientHistory))
    
        

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
            
    

    
        
    



    
    
    

