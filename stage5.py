import random

words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N\n")
word = random.choice(words)

solution = '-' * len(word)
print(solution)
solution = list(solution)

for j in range(8):
    print("Input a letter: \n")

    player_input = input()
    if player_input in word:
        for i in range(len(word)):
            if word[i] == player_input:
                solution[i] = player_input
    print("".join(solution))

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
