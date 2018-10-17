# Manipulates overpartitions as python lists

print('Hello, World!')

def partitions(n):
    list = []
    for part in range(n + 1)[:0:-1]:
        if part == n:
            list.append([part])
        for partition in partitions(n - part):
            new = [part]
            new += partition
            list.append(new)
    return list

def overpartitions_bounded(n, max):
    list = []
    for part in range(max + 1)[:0:-1]:
        for multiplicity in range(n//part + 1)[:0:-1]:
            if part*multiplicity == n:
                new = [part for i in range(multiplicity)]
                new_ovr = [-part] + [part for i in range(multiplicity - 1)]
                list.append(new)
                list.append(new_ovr)
            for partition in overpartitions_bounded(n - part*multiplicity, part - 1):
                new = [part for i in range(multiplicity)]
                new += partition
                new_ovr = [-part] + [part for i in range(multiplicity - 1)]
                new_ovr += partition
                list.append(new)
                list.append(new_ovr)
    return list

def overpartitions(n):
    return overpartitions_bounded(n,n)

def D_rank(overpartition):
    return abs(overpartition[0]) - len(overpartition)

def dissect_mod_4(ovr):
    ovr0, ovr1, ovr2, ovr3 = [], [], [], []
    for part in ovr:
        int = abs(part)
        if int % 4 == 0:
            ovr0.append(part)
        elif int % 4 == 1:
            ovr1.append(part)
        elif int % 4 == 2:
            ovr2.append(part)
        else:
            ovr3.append(part)
    return(ovr0, ovr1, ovr2, ovr3)
