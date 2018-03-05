def add_up(li, n):
    left = 0
    right = len(li) - 1
    count = 0
    while left < right:
        if li[left] + li[right] == n:
            count += 1
            right -= 1
        elif li[left] + li[right] > n:
            right -= 1
        else:
            left += 1
    return count


li = [0, 2, 4, 6, 8, 8, 10, 16]
print(add_up(li, 16))
