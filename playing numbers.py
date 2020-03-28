from math import *
import time
# naive approach
# def catalan(n):
#     if n <= 1:
#         return 1
#
#     res = 0
#     for i in range(n):
#         res += catalan(i) * catalan(n - i - 1)
#     return res

"""
# dynamic programming
def catalan1(n):
    if n == 0 or n == 1:
        return 1

    cat = [0 for _ in range(n + 1)]

    cat[0] = 1
    cat[1] = 1
    for i in range(2, n + 1):
        # cat[i] = 0
        for j in range(i):
            cat[i] = cat[i] + cat[j] * cat[i - j - 1]
    return cat[n]


t0 = time.perf_counter()
for i in range(15):
    print(catalan(i))
t1 = time.perf_counter()
tn = t1-t0

t0 = time.perf_counter()
for i in range(15):
    print(catalan1(i))
t1 = time.perf_counter()
tdp = t1-t0

print(tn, tdp)
"""
# backtracking
"""
count = 0
tc = 0
def dice_sum(n, sum, li):
    global tc
    tc += 1
    if n == 0 and sum == 0:
        global count
        count += 1
        print(li)
        return
    elif n <= sum <= n * 6:  # to improve the time complexity by avoiding unnecessary calls
        for x in range(1, 7):
            temp = li + [x]
            dice_sum(n-1, sum-x, temp)
        return


dice_sum(3, 7, [])
print(count, tc)
"""

"""
# permutation 
def permutation(string, res):
    if len(string) == 1:
        res.append(string)
        print(res)
        return
    else:
        for i in range(len(string)):
            st = string[0:i] + string[i+1:]
            k = res + [string[i]]
            permutation(st, k)
        return


s = 'abc'
permutation(s, [])
"""


def per(res, arr, temp):
    if len(temp) == 3:
        res.append(temp[:])
        return
    else:
        for x in range(len(arr)):
            it = arr[x]
            temp.append(it)
            arr.remove(it)
            # print(arr, temp)
            per(res, arr, temp)
            arr.insert(x, it)
            temp.pop()
        return


result = []
li = [1, 1, 3]
# per(result, li, [])
print(result)

s = ['0', '1', '2', '3']
a = s[:]
print(id(a), id(s))

# sublist
# def sublist(arr, temp):
#     if len(arr) == 0:
#         print(temp)
#         return
#     else:
#         first = arr[0]
#         x = temp + [first]
#         arr.remove(first)
#         sublist(arr, temp)
#         sublist(arr, x)
#         # must un-chosen otherwise the program won't work
#         arr.insert(0, first)
#         return
#
#
# li = ['James', 'Curry', 'Kobe', 'Lin']
# sublist(li, [])


def search(nums, t):
    low, h = 0, len(nums)-1
    while low < h:
        mid = (low+h) // 2
        a = nums[0] > nums[mid]
        b = nums[0] > t
        if a == b:
            if nums[mid] < t:
                low = mid + 1
            else:
                h = mid

        elif b:
            low = mid + 1
        else:
            h = mid

        if nums[mid] == t:
            return mid
    return -1


arr = [3, 4, 5, 6, 7, 8, -2, -1, 0, 1, 2]
target = 6
ans = search(arr, target)
print(ans)


