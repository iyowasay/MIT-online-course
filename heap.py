import random


def swap(a, m, n):
    a[m], a[n] = a[n], a[m]


def create_array(ss, maximum):
    return [random.randint(0, maximum) for i in range(ss)]


def heapify(li, end, i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    maxi = i
    if l < end and li[i] < li[l]:
        maxi = l
    if r < end and li[maxi] < li[r]:
        maxi = r
    if maxi != i:
        swap(li, i, maxi)
        heapify(li, end, maxi)


def heap_sort(li):
    end = len(li)
    start = end // 2 - 1
    # build max heap
    for i in range(start, -1, -1):
        heapify(li, end, i)
    for i in range(end-1, 0, -1):
        swap(li, i, 0)
        heapify(li, i, 0)
    return li


lu = create_array(13, 50)
print(lu)
print(heap_sort(lu))
# def heap_sort(li):
#     unsorted_index = len(li)
#     # build max heap
#     for n in range(unsorted_index//2-1, -1, -1):
#         max_heapify(li, n, unsorted_index)
#
#     for nn in range(len(li)-1, 0, -1):
#         swap(li, nn, 0)
#         max_heapify(li, nn, 0)
#         print(li)
#     return li
#
#
# def max_heapify(li, k, end):
#     child_left = 2*k+1
#     child_right = 2*k+2
#     maxi = k
#     if child_left < end and li[k] < li[child_left]:
#         maxi = child_left
#     if child_right < end and li[maxi] < li[child_right]:
#         maxi = child_right
#     if maxi != k:
#         swap(li, k, maxi)
#         max_heapify(li, maxi, end)





