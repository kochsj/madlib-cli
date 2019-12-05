import sys

def create_list_of_inputs(file):
    idx, left_idx, list_of_prompts = 1, 0, [('', 0, -1)]
    while '}' in file[left_idx:]:
        left_idx = file.find('{', (list_of_prompts[idx-1][2]+1))
        right_idx = file.find('}', (list_of_prompts[idx-1][2]+1))
        list_of_prompts.append((file[left_idx:right_idx + 1], left_idx, right_idx))
        idx += 1
    return list_of_prompts

def construct_the_madlib(file):
    madlib, idx, prompt_list = '', 1, create_list_of_inputs(file)
    while idx < (len(prompt_list)-1):
        response = input('Enter ' + prompt_list[idx][0] + ': ')
        if response.lower() == 'quit':
            return
        madlib += file[(prompt_list[idx-1][2]+1):prompt_list[idx][1]] + response
        idx += 1

    madlib += file[(prompt_list[idx-1][2]+1):]
    print_and_create_madlib_file(madlib)

def print_and_create_madlib_file(madlib):
    print('\n'*3)
    print('*'*100)
    print('*'*100, end="\n"*2)
    print(madlib, end="\n"*2)
    print('*'*100)
    print('*'*100)
    new_madlib = open('new_madlib.txt', "w+")
    new_madlib.write(madlib)

def print_intro_message():
    print('*'*51)
    print('*'*51)
    print('*'*5, ' '*39, '*'*5)
    print('*'*5, ' '*8, '~ MADLIBS™ CLI GAME ~', ' '*8, '*'*5)
    print('*'*5, ' '*39, '*'*5)
    print('*'*5, ' '*39, '*'*5)
    print('*'*5, ' '*4, 'Respond to the prompts below!', ' '*4, '*'*5)
    print('*'*5, ' '*3, 'Prompts may ask you for a noun,', ' '*3, '*'*5)
    print('*'*5, ' '*3, 'verb, pronoun, first name, etc.', ' '*3, '*'*5)
    print('*'*5, ' '*39, '*'*5)
    print('*'*5, ' '*2, 'MadLibs™ will use your responses,', ' '*2, '*'*5)
    print('*'*5, ' '*4, 'to create a wacky cool story!', ' '*4, '*'*5)
    print('*'*5, ' '*5, "Type 'start' to get started!", ' '*4, '*'*5)
    print('*'*5, ' '*9, "Type 'quit' to exit.", ' '*8, '*'*5)
    print('*'*5, ' '*39, '*'*5)
    print('*'*51)
    print('*'*51, end="\n"*3)

########################
# file operations:
########################

print_intro_message()

try:
    file = open("template.txt").read()
except FileNotFoundError:
    print('No madlib template file found. Please assign the correct file to the file variable.')
    sys.exit()

while True:
    response = input('--> ').lower()
    if response == 'quit':
        break
    if response == 'start':
        construct_the_madlib(file)
    else:
        print("Please type 'start' to get started. Or 'quit' to quit")
