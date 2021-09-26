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
        if self.nov.size == 0:
            return(0)
        w1 = np.count_nonzero(self.nov == 1)
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

a = Overpartition.from_neg_list([8])
print(a)
print(a.weight())
print(a.d_rank())
print(a.res1crank())
f = a.frob_rep_1()

print(f[0])
print(f[1])
