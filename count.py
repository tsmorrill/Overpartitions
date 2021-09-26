import csv
from optn import optn

Overpartition = optn.Overpartition

for n in range(4):
    print("n = {}".format(n))
    print("")
    filename = "data/{}.csv".format(str(n))

    optn_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            list = [int(string) for string in line if string != "0"]
            optn_list.append(Overpartition.from_neg_list(list))

    print("There are {} overpartitions of {}:".format(len(optn_list), n))
    print("")

    crank_counts = [0 for _ in range(n)]
    frob_counts = [0 for _ in range(n)]

    for pi in optn_list:
        crank = pi.res1crank()
        if crank > 0:
            for j in range(crank):
                crank_counts[j] += 1

        print(pi)

        top, bottom = pi.frob_rep_1()

        for j in range(n):
            count = top.nov_count(j) + bottom.nov_count(j) - bottom.ov_count(j)
            frob_counts[j] += count

        print("({})".format(top.str(separator=" ")))
        print("({})".format(bottom.str(separator=" ")))
        print("")

    for j in range(n):
        print("There are {} overpartitions with crank > {}."
              .format(crank_counts[j], j))
        print("There are {} {}'s in the first Frobenius representations."
              .format(frob_counts[j], j))
        print("")
