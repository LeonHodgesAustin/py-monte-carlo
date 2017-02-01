import multiprocessing
import sys
from gamblers.simple_bettor import simple_bettor
from gamblers.double_bettor import double_bettor
from games.roll_dice import roll_dice
from timeit import default_timer as timer
# from table import table
import random


def main(args=None):
    """The Main function"""
    if args is None:
        args = sys.argv[1:]
    from table import table
    table_count = 100
    players_at_table = 100
    starting_funds = 1000000
    # initial_wager = 100
    while True:
        wager_size = random.uniform(1.0, 1000.00)
        wager_count = random.uniform(10.0, 10000)
        # player_count = 10000
        ret = 0
        player_results = []
        table_results = []

        busts = 0
        profits = 0

        args = [starting_funds,
                wager_size,
                wager_count,
                roll_dice,
                players_at_table]

        # test = table(args)
        # print test

        pool = multiprocessing.Pool(processes=13)

        start = timer()
        table_results = pool.map(table, [args]*table_count)
        end = timer()
        for t in table_results:
            for player in t:
                player_results.append(player)

        # print player_results
        player_result_max = player_results[0]
        player_result_min = player_results[0]

        for result in player_results:
            ret += result
            if result > player_result_max:
                player_result_max = result
            if result < player_result_max:
                player_result_min = result
            if result <= 0:
                busts += 1
            elif result > starting_funds:
                profits += 1
        sample_size = len(player_results)
        player_average = ret / len(player_results)
        ROI = ret - (sample_size*starting_funds)
        total_invested = sample_size*starting_funds
        percent_ROI = (ROI/total_invested)*100.00
        # add var
        wager_size_percent = (wager_size/starting_funds)*100.00

        # print "player count:   ", len(player_results)
        # print "player average: ", player_average
        # print "Player Max:     ", player_result_max
        # print "Player Min:     ", player_result_min

        # if over 1.
        if percent_ROI > 1:
            # print '___________________________________________'
            # print 'Total invested:', total_invested
            # print 'Total Return:', ret
            # print 'ROI', ROI
            # print 'Percent ROI:', percent_ROI
            # print 'Bust Rate:', (busts/sample_size)*100.00
            # print 'Profit rate:', (profits/sample_size)*100.00
            # print 'wager size:', wager_size
            # print 'wager count:', wager_count
            # print 'wager size percentage:', wager_size_percent

            saveFile = open('monteCarlo.csv', 'a')
            saveLine = '\n' + str(percent_ROI)+',' + str(wager_size_percent) + ',' + str(wager_count)+',g'
            saveFile.write(saveLine)
            saveFile.close()

        elif percent_ROI < -1:
            # print '___________________________________________'
            # print 'Total invested:', total_invested
            # print 'Total Return:', ret
            # print 'ROI', ROI
            # print 'Percent ROI:', percent_ROI
            # print 'Bust Rate:', (busts/sample_size)*100.00
            # print 'Profit rate:', (profits/sample_size)*100.00
            # print 'wager size:', wager_size
            # print 'wager count:', wager_count
            # print 'wager size percentage:', wager_size_percent

            saveFile = open('monteCarlo.csv', 'a')
            saveLine = '\n' + str(percent_ROI)+',' + str(wager_size_percent) + ',' + str(wager_count)+',r'
            saveFile.write(saveLine)
            saveFile.close()

        print "Run Time:       ", (end - start)

if __name__ == '__main__':
    main()
