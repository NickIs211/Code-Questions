def gen(till):
    for i in range(till):
        if(i % 2):
            yield i


for i in gen(10):
    print(i)
