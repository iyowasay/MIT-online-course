import random
num_range = 100
n = 1000
d = len(str(num_range))
base = 10
data = [24, 55, 4, 111, 7, 89, 204, 0, 23]
print(data)


def create_small_list(k, j):
    return [random.randint(0, k) for _ in range(j)]


lu = create_small_list(num_range, n)


def counting_sort(li, exp1):
    n = len(li)
    result = [0] * n
    count = [0] * base
    # counting the times of each number
    for i in range(0, n):
        index = (li[i] // exp1)
        count[index % 10] += 1
    # add up the count to get the position
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = li[i] // exp1
        result[count[index % 10] - 1] = li[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(li)):
        li[i] = result[i]


def radix_sort(arr):
    # find out the biggest number of digits
    # max1 = max(arr)
    # while max1 // exp > 0:
    #     counting_sort(arr, exp)
    #     exp *= 10
    exp = 1
    for _ in range(d):
        counting_sort(arr, exp)
        exp *= 10
    return arr


print(radix_sort(data))


