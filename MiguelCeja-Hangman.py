import random

word_list = ["dog", "cat", "hat", "lucky", "money", "notes", "code", "milk", "tools", "rain"]

word = random.choice(word_list)

print(word)
letters_guessed = []
guess_left = 10
players_guess = "true"
current_guess = ""
while word != players_guess:
    print("".join(list(letters_guessed)))
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(list(output)))
    current_guess = input("type a letter:")
    letters_guessed.append(current_guess)
    if current_guess not in word:
        guess_left -= 1
        print("%s guess left" % guess_left)

    if output == word:
        print("".join(list(word)))
        print("you win")
        quit()
