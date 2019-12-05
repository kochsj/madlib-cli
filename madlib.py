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
# print('*'*5, ' '*5, "Type 'start' to get started!", ' '*4, '*'*5)
# print('*'*5, ' '*9, "Type 'quit' to exit.", ' '*8, '*'*5)
# print('*'*5, ' '*39, '*'*5)
# print('*'*51)
# print('*'*51)

f = open("example.txt").read()

def create_list_of_inputs(file):
    list_of_prompts = [('', 0, 0)]
    idx = 1
    left_idx = 0
    while '}' in file[left_idx:]:
        left_idx = file.find('{', (list_of_prompts[idx-1][2]+1))
        right_idx = file.find('}', (list_of_prompts[idx-1][2]+1))
        list_of_prompts.append((file[left_idx:right_idx], left_idx, right_idx))
        # file = file[left_idx:]
        idx += 1
    # print(list_of_prompts)
    # return list_of_prompts
create_list_of_inputs(f)
def construct_the_madlib(file):
    madlib = ''
    prompt_list = create_list_of_inputs(file)
    idx = 1
    while idx < (len(prompt_list) - 1):
        response = input('Enter ' + prompt_list[idx][0])
        madlib += file[(prompt_list[idx-1][2]+1):prompt_list[idx][1]] + response


# while True:
#     response = input('...').lower()
#     if response == 'quit':
#         break
#     if response == 'start':
#         construct_the_madlib(f)
#     else:
#         print("Please type 'start' to get started. Or 'quit' to quit")
