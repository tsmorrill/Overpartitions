# Manipulates overpartitions as Python lists
# Negative integers indicate overlined parts

import math

def partitions_distinct_bounded(n, max):
    list = []
    for part in range(max + 1)[:0:-1]:
        if part == n:
            new = [part]
            list.append(new)
        for partition in partitions_distinct_bounded(n - part, part - 1):
            new = [part] + partition
            list.append(new)
    return list

def partitions_distinct(n):
    return partitions_distinct_bounded(n, n)

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

def Joichi_Stanton(l,m):
    if m == []:
        return l
    elif m[0] >= len(l):
        print('Error: l(mu) larger than #(lambda).')
    else:
        for part in m:
            l = [l + 1 for l in l[:part]] + [-l[part]] + l[part + 1:]
        return l

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

def wipe(overpartition):
    return [abs(part) for part in overpartition]

def D_rank(overpartition):
    largest = abs(overpartition[0])
    length = len(overpartition)
    return largest - length

def D_square(overpartition):
    i = 0
    while i < len(overpartition) and abs(overpartition[i]) >= i + 1:
        i += 1
    return i

def M2_rank(overpartition):
    largest = abs(overpartition[0])
    length = len(overpartition)
    length_odd = len(dissect_overlined(dissect_mod_2(overpartition)[1])[1])
    chi = int(overpartition[0] % 2 == 1 and overpartition[0] < 0)
    return math.ceil(largest/2) - length + length_odd - chi

def dissect_overlined(overpartition):
    overlined = [part for part in overpartition if part < 0]
    partition = [part for part in overpartition if part > 0]
    return(overlined, partition)

def dissect_mod_2(overpartition):
    residue_0 = [part for part in overpartition if abs(part) % 2 == 0]
    residue_1 = [part for part in overpartition if abs(part) % 2 == 1]
    return(residue_0, residue_1)

def dissect_mod_4(overpartition):
    residue_0 = [part for part in overpartition if abs(part) % 4 == 0]
    residue_1 = [part for part in overpartition if abs(part) % 4 == 1]
    residue_2 = [part for part in overpartition if abs(part) % 4 == 2]
    residue_3 = [part for part in overpartition if abs(part) % 4 == 3]
    return(residue_0, residue_1, residue_2, residue_3)

def dissect_part_size(overpartition):
    list = []
    for i in range(abs(overpartition[0]) + 1)[::-1]:
        cluster = [part for part in overpartition if abs(part) == i]
        if cluster != []:
            list.append(cluster)
    return(list)

def tableau(overpartition):
    for part in overpartition:
        if part == 0:
            dot = '|'
        elif part < 0:
            dot = '[*]'
        else:
            dot = '[ ]'
        str = ''
        for i in range(abs(part) - 1):
            str += '[ ]'
        str += dot
        print(str)

def scale(overpartition, k):
    new = [k*part for part in overpartition]
    return new

def conjugate(overpartition):
    if overpartition == []:
        return []
    new  = [0 for i in range(abs(overpartition[0]))]
    temp = [list for list in dissect_part_size(overpartition)]
    for cluster in temp:
        multiplicity = abs(cluster[0])
        new  = [new[i] +  len(cluster) for i in range(multiplicity - 1)] + [int(math.copysign(new[multiplicity - 1] + len(cluster), cluster[0]))] + new[multiplicity:]
    new = dissect_part_size(new)
    new = [cluster[::-1] for cluster in new]
    output = []
    for cluster in new:
        output += cluster
    return output

def conjugate_pairs(list):
    pairs = []
    singletons = []
    while len(list) > 0:
        item = list.pop()
        conjugate_item = conjugate(item)
        if conjugate_item in list:
            pairs.append((item, conjugate_item))
            list.remove(conjugate_item)
        else:
            singletons.append(item)
        print(list)
    return(pairs, singletons)

def pad_length(overpartition, length):
    overpartition += [0 for i in range(length - len(overpartition))]
    return overpartition

def partitions_nonneg(n, length):
    list = [pad_length(conjugate(item), length) for item in partitions_bounded(n, length)]
    return list

def overpartitions_nonneg(n, length):
    list = [pad_length(conjugate(item), length) for item in overpartitions_bounded(n, length)]
    return list
