def most_value(items, max_weight):
    table = [[] for i in range(max_weight+1)]
    table[0] = [(0, 0)]

    def value(tupl_list): return sum(tupl[0] for tupl in tupl_list)

    def weight(tupl_list): return sum(tupl[1] for tupl in tupl_list)

    for w in range(1, max_weight+1):
        val = 0
        for item in items:
            if(item[1] <= w
                    and value(table[w-item[1]]) + item[0] > val
                    and weight(table[w-item[1]]) + item[1] <= w):
                table[w] = table[w-item[1]][:]
                table[w].append(item)
                val = value(table[w])
    return table[w][1:]


# Tuple containing (value, weight)
items = [(10, 1), (2, 3), (500, 5)]
print(most_value(items, 4))
