import random

money = 15
rounds = 0

while money > 0:
    # input("Press enter to continue")
    dice1 = random.randint(1, 6)
    print("The first dice shows a %d" % dice1)

    dice2 = random.randint(1, 6)
    print("The second dice roll is %d" % dice2)

    total = dice1 + dice2
    print("The total is %d" % total)

    if total == 7:
        print("you win")
        money += 4
    else:
        money -= 1
    print("You have $%d" % money)