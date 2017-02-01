
def dAlembert(args, return_queue=None):
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
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager
            if game():
                value += wager
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                # if value <= 0:
                #     da_busts += 1
                #     break
        elif previousWager == 'loss':
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value

            if game():
                value += wager
                previousWager = 'win'
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager

                # if value <= 0:
                #     da_busts += 1
                #     break

        currentWager += 1

    if return_queue is None:
        return value
    else:
        return_queue.put(value)
