
def double_bettor(args, return_queue=None):
    '''
    Simple bettor, betting the same amount each time.
    '''

    funds = args[0]
    initial_wager = args[1]
    wager_count = args[2]
    game = args[3]

    value = funds
    wager = initial_wager
    currentWager = 1

    # since we'll be betting based on previous bet outcome #
    previousWager = 'win'

    # since we'll be doubling #
    previousWagerAmount = initial_wager

    while currentWager <= wager_count and value > 0:
        if previousWager == 'win':
            if game():
                value += wager
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
        elif previousWager == 'loss':
            if game():
                wager = previousWagerAmount * 2
                value += wager
                wager = initial_wager
                previousWager = 'win'
            else:
                wager = previousWagerAmount * 2
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager

        currentWager += 1

    if return_queue is None:
        return value
    else:
        return_queue.put(value)
