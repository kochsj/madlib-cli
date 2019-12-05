# ###################
# Intro message
# print('*'*51)
# print('*'*51)
# print('*'*5, ' '*39, '*'*5)
# print('*'*5, ' '*8, '~ MADLIBS™ CLI GAME ~', ' '*8, '*'*5)
# print('*'*5, ' '*39, '*'*5)
# print('*'*5, ' '*39, '*'*5)
# print('*'*5, ' '*4, 'Respond to the prompts below!', ' '*4, '*'*5)
# print('*'*5, ' '*3, 'Prompts may ask you for a noun,', ' '*3, '*'*5)
# print('*'*5, ' '*3, 'verb, pronoun, first name, etc.', ' '*3, '*'*5)
# print('*'*5, ' '*39, '*'*5)
# print('*'*5, ' '*2, 'MadLibs™ will use your responses,', ' '*2, '*'*5)
# print('*'*5, ' '*4, 'to create a wacky cool story!', ' '*4, '*'*5)
# print('*'*5, ' '*9, "Type 'quit' to exit.", ' '*8, '*'*5)
# print('*'*5, ' '*39, '*'*5)
# print('*'*51)
# print('*'*51)

f = open("example.txt").read()
print(len(f))
# list_of_prompts = ['an adjective: ', 'an adjective: ', 'a first name: ', 'a past-tense verb: ', 'a first name: ', 'an adjective: ', 'an adjective: ', 'a plural noun: ', 'a large animal: ', '']

def create_list_of_inputs(file):
    list_of_prompts = []
    while '}' in file:
        right_idx = file.find('{')
        left_idx = file.find('}') + 1
        list_of_prompts.append(file[right_idx:left_idx])
        file = file[left_idx:]
    return list_of_prompts

create_list_of_inputs(f)
# while True:
#     input_counter = 0
#     a = input('Name ' + list_of_prompts[input_counter])
