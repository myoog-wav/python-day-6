'''
1. get_random_question
2. show_question
3. quit_app A exit function that quits the program.
4. show_answer
'''

import random


flashcard = [
    {'question' : 'Whats the country that borders the U.K?', 'answer' : 'Ireland'},
    {'question' : 'What year did the Chinese Communists take power?', 'answer' : '1949'},
    {'question' : 'What is the name of the Navajo in their native lanuage?', 'answer' : 'Dine'},
]

def quit_app():
    '''
    Task: Tell user goodbye
    Input: n/a
    Side Effects: Prints goodbye message
    Return: n/a
    '''

    print("Hope you are smarter than before! hopefully.")

def get_random_question(cards):
    '''
    Task: Selects Random Question in flashcard list.
    Input: Flashcard List
    Side Effects: n/a 
    Return: Flashcard
    '''
    random_card = random.choice(flashcard)
    return random_card

def show_question(card):
    '''
    Task: Shows question recieved
    Input: question card
    Side Effects: Print the question
    Return: n/a
    '''

    question = card["question"]
    print('Question:', question)

def show_answer(cards):
    '''
    Task: display answer
    Input: Question Card
    Side Effects: print the answer 
    Return: N/a
    '''

    answer = cards["answer"]
    print('Answer:', answer)

def main():

    print("----Welcome and prepare to expand your brain----", "\n")

    while True:
       random_question = get_random_question(flashcard)

       show_question(random_question)

       user_input = input('commands: show, quit ').lower().strip()

       if user_input == 'show':
           show_answer(random_question)
       elif user_input == 'quit':
           quit_app()
           break

       
    
main()