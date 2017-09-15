#!/usr/bin/python
# -*- coding: utf-8 -*-

# Question string for Stage 1

Stage_1 = \
    """
Manufacturing magnate Italian Ferruccio Lamborghini founded the company in __1__ with the objective of producing a refined grand touring car 
to compete with offerings from established marques such as __2__  .
 The company's first models, such as the 350 GT, were released in the mid-1960s and were noted for their refinement, power and __3__ .
 Lamborghini gained wide acclaim in 1966 for the Miura sports coupé, which established rear mid-engine, rear __4__ drive as the standard 
 layout for high-performance __5__ of the era.

options : 1963, Ferrari, comfort, wheel, cars,lambo,sports
"""

# Options for Stage 1

Stage_1_options = ['1963', 'Ferrari', 'comfort', 'wheel', 'cars']

# Question string for Stage 2

Stage_2 = \
    """The history of iPhone began with a request from inventor Steve __1__ to __2__  Inc.'s engineers, asking them
     to investigate the use of touchscreen devices and tablet computers (which later came to fruition with the iPad).
     Many have noted the device's similarities to Apple's previous touch-screen portable __3__ , the Newton MessagePad.Like the 
     Newton, the __4__ is nearly all screen. Its form factor is credited to Apple's Chief Design __5__, Jonathan Ive.

options : Jobs, Apple, device, Ipad, iPhone, Officer ,jukebox 
     """

# Options for Stage 2

Stage_2_options = ['Jobs', 'Apple', 'device', 'iPhone', 'Officer']

# Question string for Stage 3

Stage_3 = \
    """"Emporio Armani was founded in 1975 by Giorgio __1__, fashions most influential and celebrated __2__  
    designer from __3__ . Armani provides quality, sophisticated and timeless style __4__ ranging from __5__ 
    garments, apparel, jewellery and aftershaves. The company describes themselves as “providing quality, sophistication 
    and style-timeless values with __6__ appeal.

options : Armani, fashion, France, Italy, clothing, luxury, global, Blogs, TEES
    """

# Options for Stage 3

Stage_3_options = ['Armani', 'fashion', 'Italy', 'clothing', 'luxury','global']

# question string for Stage 4

Stage_4 = \
    """In 1926 Antonio Cavalieri __1__ and his three sons, Adriano, Marcello, and Bruno Cavalieri Ducati.
    founded Società Scientifica Radio Brevetti Ducati in Bologna to produce vacuum __2__ , condensers and other radio components.
    In 1935 they had become successful enough to enable __3__  of a new factory in the Borgo Panigale area of the city. 
    Production was maintained during __4__ War II, despite the Ducati factory being a repeated target of Allied __5__.


options : Ducati , tubes , construction , War , World , bombing , Bold , Bike , Sports
    """

# Options for Stage 4

Stage_4_options = ['Ducati', 'tubes', 'construction', 'World', 'bombing']


def Main_Area():


    Stage = \
        raw_input('''Enter
easy for Stage 1
medium for Stage 2
hard for Stage 3
master for Stage 4
''')
    if Stage == 'easy':
        print str(Stage_1)
        game_code(Stage_1, Stage_1_options)
    elif Stage == 'medium':
        print Stage_2
        game_code(Stage_2, Stage_2_options)
    elif Stage == 'hard':
        print str(Stage_3)
        game_code(Stage_3, Stage_3_options)
    elif Stage == 'master':
        print str(Stage_4)
        game_code(Stage_4, Stage_4_options)
    else:
        print 'You entered a wrong choice!!, please enter a correct one\n'
        Main_Area()


def game_code(madlibs_string, Options_list):

     # length_C variable is used to iterate the loop

    length_C = 0

        # count variable is used to count the number of wrong attempts given to the user.

    count = 5

        # replacement variable is initialized with the question string and later will be replacementd with the question string having blanks replaced by the Options

    replacement = madlibs_string

        # myF1 variable is used as a parameter inside the myF function

    myF1 = 1
    while length_C < len(Options_list):
        Options = raw_input('fill in the blank __'
                           + str(length_C + 1) + '__ ?\n')
        if option_correct(Options, Options_list[length_C]):
            replacement = replacement_madlibs_string(replacement, length_C, Options)
            length_C = length_C + 1
        else:
            count = count - 1
            print 'NOT a VALID OPTION,THINK AGAIN AND TYPE ' + str(count) \
                + 'ATTEMPTS LEFT, YOU ARE ABOUT TO BE DESTROYED'
            warning_warning = 3
            if count < warning_warning:
                myF1 = 0
                break
    myF(myF1)


def myF(input):

    default_myF = 0
    if input == default_myF:
        print 'Sorry, You lost!!'
    else:
        print 'All the options were correct!!'


def option_correct(user_Options, correct_Options):

    if user_Options == correct_Options:
        return True
    else:
        return False


def replacement_madlibs_string(question, blank_index, user_Options):
 
    question = question.split()

        # index is used to store the index of the first blank in the question

    index = question.index('__' + str(blank_index + 1) + '__')

        # blank string is replaced by the next line of code

    question[index] = question[index].replace('__' + str(blank_index
            + 1) + '__', user_Options)
    question = ' '.join(question)
    print question + '\n'
    print 'Correct Options'
    return question


Main_Area()
