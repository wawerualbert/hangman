import random
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")

random_word = random.choice(word_list)
word_seal = "-" *(len(random_word)) # ------
reveal = list(word_seal) # just a list ------
    
i = 0

while i < 8: # 8 tries to input a letter
    print()
    print(word_seal) # -------
    guess = input('Input a letter: ') # dont put > at the end
    n = 0 
    while n < len(random_word): # check the input letter as many times as the length of word
        if guess == random_word[n]: # check each character in that word if the input charactor match
            reveal[n] = guess # replace - in list with the input charactor --a---
            word_seal = "".join(reveal) # make word_seal become like list reveal --a---
            n += 1
        else:
            n += 1
            
    if guess not in word_seal:
        print('No such letter in the word')
    i += 1 # count the try

print('''
Thanks for playing!
We'll see how well you did in the next stage''')
# second version
# import random

# words = ['python', 'java', 'kotlin', 'javascript']
# print("H A N G M A N\n")
# word = random.choice(words)

# solution = '-' * len(word)
# print(solution)
# solution = list(solution)

# for j in range(8):
#     print("Input a letter: \n")

#     player_input = input()
#     if player_input in word:
#         for i in range(len(word)):
#             if word[i] == player_input:
#                 solution[i] = player_input
#     print("".join(solution))

# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")
