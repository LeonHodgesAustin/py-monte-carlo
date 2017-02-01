
def simple_bettor(args, return_queue=None):
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
    while currentWager <= wager_count and value > 0:
        # print value
        if game():
            value += wager
        else:
            value -= wager
        currentWager += 1

    if return_queue is None:
        return value
    else:
        return_queue.put(value)
