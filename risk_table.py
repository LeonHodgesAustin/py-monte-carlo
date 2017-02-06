import threading
import Queue

from games.risk_dice import risk_dice


def risk_table(args):
    '''
    Simple table for gamblers
    '''
    pool = []
    queue = Queue.Queue()
    player_results = []
    players_at_table = args[0]
    attackers = [1, 2, 3]
    defenders = [1, 2]
    i = 0
    while i < players_at_table:
        for attacker in attackers:
            for defender in defenders:
                if attacker >= defender:
                    # print "Attackers: " + str(attacker)
                    # print "defenders: " + str(defender)
                    play_game(attacker, defender, queue, pool, player_results)
                    i += 1
    for thread in pool:
        thread.join()

    return player_results


def play_game(attacker, defender, queue, pool, player_results):
    t = threading.Thread(target=risk_dice, args=(attacker, defender, queue))
    pool.append(t)
    t.start()  # are these threads actaully concurrent?
    response = queue.get()
    player_results.append(response)
