import numpy as np

class Overpartition:

    def __init__(self, ov, nov):
        self.ov = ov
        self.nov = nov

    def __str__(self):
        return self.str()

    def __repr__(self):
        ov, nov = list(self.ov), list(self.nov)
        return(str([ov, nov]))

    def str_list(self):
        ov, nov = list(self.ov), list(self.nov)
        part_list = ov + nov
        part_list.sort(reverse = True)
        for part in ov:
            part_list[part_list.index(part)] = "/" + str(part)
        return([str(item) for item in part_list])

    def str(self, separator = " + "):
        string = separator.join(self.str_list())
        if string == "":
            return("None")
        return(string)

    def weight(self):
        if self.ov.size == 0:
            ov_weight = 0
        else:
            ov_weight = np.sum(self.ov)
        if self.nov.size == 0:
            nov_weight = 0
        else:
            nov_weight = np.sum(self.nov)
        return(ov_weight + nov_weight)

    def max(self):
        if self.ov.size == 0:
            ov_max = 0
        else:
            ov_max = self.ov[0]
        if self.nov.size == 0:
            nov_max = 0
        else:
            nov_max = self.nov[0]
        return(max(ov_max, nov_max))

    def len(self):
        return(self.ov.size + self.nov.size)

    def ov_count(self, part):
        return(np.count_nonzero(self.ov == part))

    def nov_count(self, part):
        return(np.count_nonzero(self.nov == part))

    def d_rank(self):
        return(self.max() - self.len())

    def res1crank(self):
        if self.nov.size == 0:
            return(0)
        w1 = self.nov_count(1)
        m1 = np.count_nonzero(self.nov > w1)
        if w1 == 0:
            res1crank = max(self.nov)
        elif w1 == 1 and m1 == 0:
            res1crank = 1
        else:
            res1crank = m1 - w1
        return(res1crank)

    def frob_rep_1(self):
        ov, nov = list(self.ov), list(self.nov)
        top = []
        bottom_ov, bottom_nov = [], []

        while len(ov) + len(nov) > 0:
            if len(ov) == 0:
                max_ov = 0
            else:
                max_ov = ov[0]
            if len(nov) == 0:
                max_nov = 0
            else:
                max_nov = nov[0]

            if max_ov >= max_nov:
                top.append(ov.pop(0))
                bottom_nov.append(len(nov))
                nov = [part - 1 for part in nov if part > 1]
            else:
                top.append(nov.pop(0))
                bottom_ov.append(len(nov))
                nov = [part - 1 for part in nov if part > 1]

        top = [part - 1 for part in top]
        top = Overpartition.from_neg_list(top)
        bottom = Overpartition.from_list_pair(bottom_ov, bottom_nov)
        return(top, bottom)

    @classmethod
    def from_list_pair(cls, ov, nov):
        ov = list(set(ov))
        ov.sort(reverse=True)
        ov = np.array(ov)
        nov.sort(reverse=True)
        nov = np.array(nov)
        return cls(ov, nov)

    @classmethod
    def from_neg_list(cls, neg_list):
        ov, nov = [], []
        for part in neg_list:
            if part < 0:
                ov.append(-part)
            else:
                nov.append(part)
        return cls.from_list_pair(ov, nov)

a = Overpartition.from_neg_list([9,-9, 5, 4, 2, 2, -1])
print(a)
print("weight: {}".format(a.weight()))
print("Dyson rank: {}".format(a.d_rank()))
print("first residual crank: {}".format(a.res1crank()))
f = a.frob_rep_1()
print("First Frobenius representation:")
print(f[0].str(separator=" "))
print(f[1].str(separator=" "))
