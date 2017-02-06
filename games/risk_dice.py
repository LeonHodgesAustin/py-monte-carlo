import random


def risk_dice(attack, defend, return_queue=None):
    # print attack
    # print defend
    attack_dice = []
    defence_dice = []
    wins = 0

    for i in range(attack):
        attack_dice.append(roll_d6())
    attack_dice.sort()

    for i in range(defend):
        defence_dice.append(roll_d6())
    defence_dice.sort()

    # print "comapering"
    # print range(defend)
    # print attack_dice
    # print defence_dice
    for i in range(defend):
        if attack_dice[i] > defence_dice[i]:
            wins += 1

    if return_queue is None:
        return [attack, defend, wins]
    else:
        return_queue.put([attack, defend, wins])


def roll_d6():
    return random.randint(1, 6)
