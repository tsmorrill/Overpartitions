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

    def str(self, seperator = " + "):
        ov, nov = list(self.ov), list(self.nov)
        part_list = ov + nov
        part_list.sort(reverse = True)
        for part in ov:
            part_list[part_list.index(part)] = "/" + str(part)
        string = seperator.join([str(item) for item in part_list])
        return(string)

    def weight(self):
        return(np.sum(self.ov) + np.sum(self.nov))

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

    def d_rank(self):
        return(self.max() - self.len())

    def res1crank(self):
        w1 = np.count_nonzero(self.nov == 1)
        m1 = np.count_nonzero(self.nov > w1)
        if self.len == 0:
            res1crank = 0
        elif w1 == 0:
            res1crank = max(self.nov)
        elif w1 == 1 and m1 == 0:
            res1crank = 1
        else:
            res1crank = m1 - w1
        return(res1crank)

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

a = Overpartition.from_neg_list([-3,-2,-1,1])
print(a)
print(a.weight())
print(a.d_rank())
print(a.res1crank())
