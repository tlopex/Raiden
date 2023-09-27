import getpass
def record_myscore(My):
    Record = open('RankData/rank.txt', "a")

    record_list = {'name':str(getpass.getuser()), 'score' : My.score, 'HP': My.life}
    Record.write(str(record_list) + '\n')
    Record.close()