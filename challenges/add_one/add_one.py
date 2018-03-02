def add_one(number):
    carry = 1
    for i in range(len(number)-1, -1, -1):
        number[i] += carry
        carry = 0
        if number[i] >= 10:
            carry = int(number[i]/10)
        number[i] %= 10
    if carry != 0:
        number.insert(0, carry)
    return number


number = [9, 9, 9, 9]
print(add_one(number))
number = [1, 2, 3, 3]
print(add_one(number))
