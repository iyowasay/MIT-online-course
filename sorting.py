import random
import time


# insertion sort
def insertion_sort(li):
    for sort_len in range(1, len(li)):
        cur_item = li[sort_len]
        insert_index = sort_len

        while insert_index > 0 and cur_item < li[insert_index-1]:
            li[insert_index] = li[insert_index-1]
            insert_index -= 1
        li[insert_index] = cur_item
    return li

    # key = 1
    # while key < len(li):
    #     c = key
    #     for i in range(key-1, -1, -1):
    #         a, b = li[c], li[i]
    #         if a >= b:
    #             break
    #         else:
    #             li[c] = b
    #             li[i] = a
    #             c -= 1
    #     key += 1
    # return li


# bubble sort
def bubble_sort(li):
    swapped = True
    while swapped:
        swapped = False
        for k in range(len(li)-1):
            if li[k] > li[k+1]:
                li[k], li[k+1] = li[k+1], li[k]
                swapped = True
            # if not swapped:
            # break
    return li


# selection sort
def selection_sort(li):
    sort_len = 0  # the index of unsorted part
    while sort_len < len(li):
        min_index = None
        for i, elem in enumerate(li[sort_len:]):
            if min_index is None or elem < li[min_index]:
                min_index = i + sort_len
        li[sort_len], li[min_index] = li[min_index], li[sort_len]
        sort_len += 1
    return li


# merge sort
def create_array(ss, maximum):
    return [random.randint(0, maximum) for _ in range(ss)]
    # array = []
    # for i in range(size):
    #     num = random.randint(0, maximum)
    #     array.append(num)
    # return array


def merge(l, r):
    result_array = []
    l_index, r_index = 0, 0
    while len(result_array) < len(l)+len(r):
        if l[l_index] > r[r_index]:
            result_array.append(r[r_index])
            r_index += 1
        else:
            result_array.append(l[l_index])
            l_index += 1

        if l_index == len(l):
            result_array.extend(r[r_index:])
        elif r_index == len(r):
            result_array.extend(l[l_index:])
    return result_array


def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li)//2
    a, b = merge_sort(li[:mid]), merge_sort(li[mid:])
    return merge(a, b)


# quick sort
def partition(li, left, right, pivot):
    while left <= right:
        while li[left] < pivot:
            left += 1

        while li[right] > pivot:
            right -= 1

        if left <= right:
            # swapped the elements
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1
    return left


def quick_sort1(li, left, right):
    if left >= right:
        return
    pivot = li[(left + right)//2]
    index = partition(li, left, right, pivot)
    quick_sort1(li, left, index - 1)
    quick_sort1(li, index, right)
    return li


def quick_sort2(li):
    if len(li) <= 1:
        return li
    pivot = li[random.randint(0, len(li)-1)]
    smaller, equal, larger = [], [], []
    for x in li:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort2(smaller)+equal+quick_sort2(larger)


nn = [10, 100, 1000, 6000]
times = {'bubble': [], 'selection': [], 'insertion': [], 'merge': [], 'quick': []}

for j in nn:
    lu = create_array(j, j)
    t1 = time.perf_counter()
    insertion_sort(lu)
    t2 = time.perf_counter()
    times['insertion'].append(t2-t1)

    lu = create_array(j, j)
    t1 = time.perf_counter()
    quick_sort1(lu, 0, len(lu)-1)
    t2 = time.perf_counter()
    times['quick'].append(t2 - t1)

    lu = create_array(j, j)
    t1 = time.perf_counter()
    merge_sort(lu)
    t2 = time.perf_counter()
    times['merge'].append(t2 - t1)

    lu = create_array(j, j)
    t1 = time.perf_counter()
    bubble_sort(lu)
    t2 = time.perf_counter()
    times['bubble'].append(t2 - t1)

    lu = create_array(j, j)
    t1 = time.perf_counter()
    selection_sort(lu)
    t2 = time.perf_counter()
    times['selection'].append(t2 - t1)


print('Table \tBubble  \tInsertion  \tSelection  \tMerge   \tQuick')
print(60*"-")
for i, size in enumerate(nn):
    print(str(size) + '\t{:^8.5f}\t{:8.5f}\t{:^8.5f}\t{:^8.5f}\t{:^8.5f}\t'.format(times['bubble'][i], times['insertion'][i], times['selection'][i], times['merge'][i], times['quick'][i],))
