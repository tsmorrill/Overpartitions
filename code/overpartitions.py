# Manipulates overpartitions as python lists

import math

print('Hello, World!')

def partitions_bounded(n, max):
    list = []
    for part in range(max + 1)[:0:-1]:
        for multiplicity in range(n//part + 1)[:0:-1]:
            if part*multiplicity == n:
                new = [part for i in range(multiplicity)]
                list.append(new)
            for partition in partitions_bounded(n - part*multiplicity, part - 1):
                new = [part for i in range(multiplicity)]
                new += partition
                list.append(new)
    return list

def partitions(n):
    return partitions_bounded(n, n)

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

def weight(overpartition):
    return sum(abs(part) for part in overpartition)

def forgetful(overpartition):
    return [abs(part) for part in overpartition]

def D_rank(overpartition):
    largest = abs(overpartition[0])
    length = len(overpartition)
    return largest - length

def M2_rank(overpartition):
    largest = abs(overpartition[0])
    length = len(overpartition)
    length_odd = len(dissect_overlined(dissect_mod_2(overpartition)[1])[1])

def dissect_overlined(ovr):
    ovr0, ovr1 = [], []
    for part in ovr:
        if part < 0:
            ovr0.append(part)
        else:
            ovr1.append(part)
    return(ovr0, ovr1)

def dissect_mod_2(ovr):
    ovr0, ovr1 = [], []
    for part in ovr:
        int = abs(part)
        if int % 2 == 0:
            ovr0.append(part)
        else:
            ovr1.append(part)
    return(ovr0, ovr1)

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
