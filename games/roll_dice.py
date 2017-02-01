import random


def roll_dice():
    roll = random.randint(1, 100)

    if roll <= 51:
        return False
    elif roll > 51:
        return True
