def ranklist():
    record = open("RankData/rank.txt", "r")
    ranklist = []
    while True:
        line = record.readline()
        if line == '':
            break
        line = line.rstrip().split()
        ranklist.append([line[1][1:-2], int(line[3][:-1]), line[5][:-1]])


    ranklist.sort(key = lambda x: x[1], reverse=True)
   # for each in ranklist:
     #   print(each)
    return ranklist
if __name__ == '__main__':
    ranklist()