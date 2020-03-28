# Knapsack problem - pseudo polynomial time
from random import *
bag_size = 10
num = 6
value_size = 5
weight_size = 5
things = [(randint(1, value_size), randint(1, weight_size)) for _ in range(num)]
# things = sorted(things)
print(things)

for i in range(len(things)):
    if things[i][1] > bag_size:
        things.pop(i)
        num -= 1


# naive recursive implementation with O(2^n) time
def knapsack1(n, remain_weight, li):
    if n == 0 or remain_weight <= 0:
        return 0

    if li[n-1][1] > remain_weight:
        return knapsack1(n-1, remain_weight, li)
    else:
        return max(li[n-1][0]+knapsack1(n-1, remain_weight-li[n-1][1], li), knapsack1(n-1, remain_weight, li))


# use memoization to improve the complexity to O(num * bag_size)
arr = [[None]*(bag_size+1) for _ in range(num+1)]
itl = []


def knapsack2(x, remain_weight, li):
    result_item = []
    # if remain_weight > 0 and x < num:
    if arr[x][remain_weight] is not None:  # != 0 may cause some problem
        return arr[x][remain_weight]
    if x == num or remain_weight == 0:
        v = 0
    elif li[x][1] <= remain_weight:
        v = max(knapsack2(x+1, remain_weight-li[x][1], li) + li[x][0], knapsack2(x+1, remain_weight, li))

    else:
        v = knapsack2(x+1, remain_weight, li)

    arr[x][remain_weight] = v
    return v


# using bottom-up manner
K = [[0 for _ in range(bag_size + 1)] for _ in range(num + 1)]

def knapsack3(x, remain_weight, li):
    for i in range(x + 1):
        for w in range(remain_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif li[i - 1][1] <= w:
                K[i][w] = max(li[i - 1][0] + K[i - 1][w - li[i - 1][1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[x][remain_weight]

# find out the items that you should take
items =[]
def item(r, c, tab, li):
    if r >= 0 and c >= 0:
        if tab[r][c] == tab[r-1][c]:
            return item(r-1, c, tab, li)
        else:
            items.append(li[r-1])
            return item(r-1, c-li[r-1][1], tab, li)


print(knapsack1(num, bag_size, things))
print(knapsack2(0, bag_size, things))
print(knapsack3(num, bag_size, things))
item(num, bag_size, K, things)
print(items)

for o in range(num+1):
    print(K[o])




















