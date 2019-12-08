# from madlib import print_and_create_madlib_file, print_intro_message, construct_the_madlib, create_list_of_inputs
from madlib import construct_the_madlib, create_list_of_inputs




# https://code-maven.com/mocking-input-and-output-for-python-testing

# def test_madlib():
#     string = "I, the {Adjective} and {Adjective} {A First Name}, have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}! What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."

#     input_values = ['red', 'grey', 'sally', 'cried', 'emily', 'cold', 'tall', 'clocks', 'horse', 'mouse', 'mary', 'hot', 'glasses', 'heavy', 'spatulas', '23', 'max', '7', 'beers', '800', 'hammers']

#     output = []

#     def mock_input(s):
#         output.append(s)
#         return input_values.pop(0)
#     construct_the_madlib.input = mock_input
#     construct_the_madlib.print = lambda s : output.append(s)

#     construct_the_madlib(string)

#     assert output == [

#     ]

