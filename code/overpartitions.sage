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

def overpartitions(n, max):
    list = []
    for part in range(max + 1)[:0:-1]:
        for multiplicity in range(floor(n/part) + 1)[:0:-1]:
            if part*multiplicity == n:
                new = [part for i in range(multiplicity)]
                new_ovr = [-part] + [part for i in range(multiplicity - 1)]
                list.append(new)
                list.append(new_ovr)
            for partition in overpartitions(n - part*multiplicity, part - 1):
                new = [part for i in range(multiplicity)]
                new += partition
                new_ovr = [-part] + [part for i in range(multiplicity - 1)]
                new_ovr += partition
                list.append(new)
                list.append(new_ovr)
    return list

def overpartitions_all(n):
    return overpartitions(n,n)
