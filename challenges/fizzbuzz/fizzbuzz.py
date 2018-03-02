def fizbuzz(k):
    for i in range(k):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        print(s if s != "" else i)
