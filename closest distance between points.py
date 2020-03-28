from math import *
from random import *
from collections import *

num = 1000
size = 1000
points = [(randint(0, size), randint(0, size)) for _ in range(num)]
distinct = [(sample(range(100), 1)[0], sample(range(100), 1)[0]) for _ in range(10)]
print(distinct)
# print(points)
arr = [(randint(0, 10), randint(0, 10)) for _ in range(10)]
P = [(94, 5), (96, -79), (20, 73), (8, -50), (78, 2), (100, 63), (-14, -69), (99, -8), (-11, -7), (-78, -46)]
data = [(0,0), (1,1), (-4,1), (-7,-2), (4,5)]
px = sorted(distinct, key=lambda tup: tup[0])
py = sorted(distinct, key=lambda tup: tup[1])

def distance(a, b):
    ab = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return ab


def brute_force(li):
    # pp = []
    d_min = 1e10
    for q in range(len(li)):
        for r in range(q+1, len(li)):
            if distance(li[q], li[r]) < d_min:
                d_min = distance(li[q], li[r])
                # pp = [li[q], li[r]]
    return d_min


# print(arr, brute_force(arr))


def closest_distance(li):
    pairs = [tuple()]*6
    result_points = tuple()
    li.sort(key=lambda tup: tup[0])
    n = len(li)
    mid = n // 2
    # left
    left_min, right_min = 1e10, 1e10
    for l in range(mid+1):
        for k in range(l+1, mid+1):
            d1 = distance(li[l], li[k])
            if d1 < left_min:
                left_min = d1
                pairs[0] = li[l]
                pairs[1] = li[k]
    # right
    for r in range(mid+1, n):
        for j in range(r + 1, n):
            d2 = distance(li[r], li[j])
            if d2 < right_min:
                right_min = d2
                pairs[2] = li[r]
                pairs[3] = li[j]

    d = min(left_min, right_min)
    strip = []
    for pp in li:
        if li[mid][0]-d < pp[0] < li[mid][0]+d:
            strip.append(pp)
    strip.sort(key=lambda tup: tup[1])
    d_strip = 1e10
    for m in range(len(strip)):
        for mm in range(m+1, len(strip)):
            d3 = distance(strip[m], strip[mm])
            if d3 < d_strip:
                d_strip = d3
                pairs[4] = strip[m]
                pairs[5] = strip[mm]

    minimum = min(d, d_strip)
    if minimum == d_strip:
        result_points = (pairs[4], pairs[5])
    elif minimum == right_min:
        result_points = (pairs[2], pairs[3])
    elif minimum == left_min:
        result_points = (pairs[0], pairs[1])

    return minimum, result_points

# def closest_distance_fast(li):


ans = closest_distance(data)
print(ans)


# the Tower of Hanoi
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# nn = 4
# TowerOfHanoi(nn, 'A', 'B', 'C')










