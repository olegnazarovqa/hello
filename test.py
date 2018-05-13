def positive_sum(arr):
    o = 0
    for i in arr:
        if i > 0:
            o += i
    return o

print(positive_sum([4, 2, -7, 10]))