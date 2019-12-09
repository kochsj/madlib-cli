from testable_madlib import create_list_of_inputs

# Brainstorm possible tests
# - In order to get any tests running, can you think of ways to test aspects of your code that do not use input()?

# Reading the file at the start - has to be template.txt in same directory
def test_there_is_something_in_the_file():
    expected = 'Test template\n'
    assert open('test_template.txt').read() == expected
# list of prompts in create_list_of_inputs needs to have more than 1 item in the list.
def test_file_with_no_curly():
    file = open('test_template.txt').read()
    expected = 1
    actual = len(create_list_of_inputs(file))
    assert expected == actual

def test_file_with_inputs():
    file = open('template.txt').read()
    list_of_inputs = create_list_of_inputs(file)
    assert len(list_of_inputs) > 1


# Attempt to use inputs in the test using mock_input:

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

