import multiprocessing
import sys
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


# from games.risk_dice import risk_dice


def plot_data(data):
    # plt.clf()
    # plt.title('Risk heat map')
    # plt.ylabel('y')
    # plt.xlabel('x')
    # plt.imshow(data, cmap='hot', interpolation='nearest', extent=[1, 3, 1, 3])
    # plt.show()
    # im = plt.matshow(data, cmap='hot', extent=[1, 2, 1, 3]) # pl is pylab imported a pl
    # plt.colorbar(im)
    # plt.show()
    pass


def main(args=None):
    """The Main function"""
    if args is None:
        args = sys.argv[1:]
    from risk_table import risk_table
    table_count = 10
    players_at_table = 10

    player_results = []
    table_results = []

    args = [players_at_table]

    pool = multiprocessing.Pool(processes=13)

    # print risk_table([2])

    start = timer()
    table_results = pool.map(risk_table, [args]*table_count)
    end = timer()
    for t in table_results:
        for player in t:
            player_results.append(player)
            # print player

    print "Run Time: ", (end - start)

    aggrigate_data = {}
    for result in player_results:
        try:
            aggrigate_data[(result[0], result[1])] += result[2]
        except KeyError:
            aggrigate_data[(result[0], result[1])] = result[2]

    print aggrigate_data
    matrix = [[0 for j in range(2)] for i in range(3)]
    print matrix
    for x, y in aggrigate_data:
        print x
        print y
        print aggrigate_data[(x, y)]
        matrix[x-1][y-1] = aggrigate_data[(x, y)]
        print matrix

    print np.matrix(matrix)

    # heatmap_data = []
    # for a, b in aggrigate_data:
    #     heatmap_data.append([a, b, (aggrigate_data[(a, b)] * 100)])
    # print heatmap_data
    # print np.matrix(player_results)

    # plot_data(heatmap_data)


if __name__ == '__main__':
    main()
