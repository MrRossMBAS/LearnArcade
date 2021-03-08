# Feelings generator, by Kael.
# 26/02/2021
import random


def ask_name():
    '''Asks user input and returns the name value.'''

    name = input('Enter your name: ')

    return name


def intro(name):
    '''Called once at the start of main function,
        asks for the player's name and explains the generator.'''

    user_name = name
    print('Welcome, ' + user_name + '. It\'s nice to meet you!')
    print()
    print('''By entering the feeling or the letter related to it in the menu below,
you will get a quote about that feeling automatically generated for you.''')


def question_loop(name):
    '''This is the loop that gets the answer from the user
        and generates the quote.'''

    print('''
#======================#
#       Feelings       #
#======================#
#  a) Sad              #
#  b) Happy            #
#  c) Angry            #
#  d) Tired            #
#  e) Worried          #
#  f) Optimistic       #
#  g) Amped            #
#  h) Intrigued        #
#                      #
#======================#
            ''')

    # Feelings.
    sad = 'sad'
    happy = 'happy'
    angry = 'angry'
    tired = 'tired'
    worried = 'worried'
    optimistic = 'optimistic'
    amped = 'amped'
    intrigued = 'intrigued'

    # Quote lists.
    sad_quotes = ['\'Tears come from the heart, not from the brain.\' - Unknown',
                  '\'People keep telling me that life goes on, but to me that\'s the saddest part.\' - Unknown',
                  '\'A million words would not bring you back, I know because I tried, neither would a million tears, I know because I cried.\' - Unknown']

    happy_quotes = ['\'There are so many beautiful reasons to be happy.\' - Unknown',
                    '\'If you want to be happy, do not dwell in the past, do not worry about the future, focus on living fully in the present.\' - Ray J. Bennett',
                    '\'Be happy with what you have, be excited about what you want.\' - Alan Cohen']

    angry_quotes = [
        '\'People say everything happens for a reason. So when I punch you in the face, remember I have a reason.\' - Unknown',
        '\'Speak when you are angry and you\'ll make the best speech you\'ll ever regret\' - Ambrose Brierce',
        '\'Don\'t be angry with people who don\'t have the capacity to change.\' - Unknown']

    tired_quotes = ['\'She\'s strong but she\'s exhausted.\' - R.H Sin',
                    '\'I\'m so tired even my tiredness is tired.\' - Unknown',
                    '\'I\'m exhausted from trying to be stronger than I feel.\' - Unknown']
    worried_quotes = 'worried'
    optimistic_quotes = 'optimistic'
    amped_quotes = 'amped'
    intrigued_quotes = 'intrigued'

    user_feeling = input('Enter a feeling: ')

    # -- Checking which feeling the user entered. --#

    if sad in user_feeling.lower() or user_feeling.lower() == 'a':
        # Generates a random integer that corresponds to a random quote in the list.
        random_quote_number = random.randint(0, len(sad_quotes) - 1)

        print(sad_quotes[random_quote_number])

    elif happy in user_feeling.lower() or user_feeling.lower() == 'b':
        # Generates a random integer that corresponds to a random quote in the list.
        random_quote_number = random.randint(0, len(happy_quotes) - 1)

        print(happy_quotes[random_quote_number])

    elif angry in user_feeling.lower() or user_feeling.lower() == 'c':
        # Generates a random integer that corresponds to a random quote in the list.
        random_quote_number = random.randint(0, len(angry_quotes) - 1)

        print(angry_quotes[random_quote_number])

    elif tired in user_feeling.lower() or user_feeling.lower() == 'd':
        # Generates a random integer that corresponds to a random quote in the list.
        random_quote_number = random.randint(0, len(tired_quotes) - 1)

        print(tired_quotes[random_quote_number])

    else:
        print('I apologise, ' + name + '. I do not have a quote for that feeling you have mentioned.')
        print('Try entering another!')

    question_loop(name)


def main():
    '''The main function.'''
    user_name = ask_name()
    print()  # Blank space between entering name and the welcome.
    intro(user_name)

    # Main question loop.
    question_loop(user_name)


# Main.
main()