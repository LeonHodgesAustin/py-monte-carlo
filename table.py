import threading
import Queue

from gamblers.simple_bettor import simple_bettor
from gamblers.double_bettor import double_bettor
from gamblers.dAlembert import dAlembert


def table(args):
    '''
    Simple table for gamblers
    '''
    pool = []
    queue = Queue.Queue()
    player_results = []
    players_at_table = args[4]
    for i in range(players_at_table):
        t = threading.Thread(target=dAlembert, args=(args, queue))
        pool.append(t)
        t.start()
        response = queue.get()
        player_results.append(response)
    for thread in pool:
        thread.join()

    return player_results
