def bucket_sort(data):
    nums = []
    for val in data:
        try:
            nums.append(int(val))
        except ValueError:
            continue
    li = [0] * (max(nums)+1)
    for i in range(len(nums)):
        li[nums[i]] += 1
    return [item for item, index in enumerate(li) for i in range(index)]


if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 2):
        print(bucket_sort(list(sys.argv[1:len(sys.argv)])))
    elif(len(sys.argv) == 2):
        print(bucket_sort(sys.argv[1]))
    else:
        print("No arguments passed!")
