def subsets(given):
    set = []
    for i in range(1 << len(given)):
        subset = []
        for s in range(len(given)):
            if(i & (1 << s) != 0):
                subset.append(given[s])
        set.append(subset)
    return set


given = [1, 2, 3]
print(subsets(given))
