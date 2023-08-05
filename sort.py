def quick_sort(alist, start, end):
    if start >= end:
        return None
    left = start
    right = end
    mid_data = alist[start]
    while left < right:
        while left < right and alist[right] > mid_data:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid_data:
            left += 1
        alist[right] = alist[left]

    alist[left] = mid_data
    quick_sort(alist, start, left - 1)
    quick_sort(alist, left + 1, end)
#归并排序
def merge_sort(alist):
    if len(alist) == 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge(left, right)
def merge(left, right):
    left_rep = 0
    right_rep = 0
    new_list = []
    while left_rep < len(left) and right_rep < len(right):
        if left[left_rep] < right[right_rep]:
            new_list.append(left[left_rep])
            left_rep += 1
        else:
            new_list.append(right[right_rep])
            right_rep += 1
    new_list = new_list + left[left_rep:] + right[right_rep:]
    return new_list
#希尔排序
def siery_sort(alist):
    start = 0
    skip = len(alist) // 2
    while skip > 0:
        for index in range(start + skip, len(alist), skip):
            current = alist[index]
            position = index
            while current < alist[position - skip] and position >= skip:
                alist[position] = alist[position - skip]
                position = position - skip
            alist[position] = current
        skip = skip // 2
#插入排序
def insert_sort(alist):
    for index in range(1, len(alist)):
        current = alist[index]
        position = index
        while current < alist[position - 1] and position >= 1:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current
#选择排序
def select_sort(alist):
    for i in range(len(alist) - 1):
        max_index = 0
        for index in range(len(alist) - i):
            if alist[max_index] < alist[index]:
                max_index = index
        alist[len(alist) - i - 1], alist[max_index] = \
            alist[max_index], alist[len(alist) - i - 1]
#冒泡排序// You try again exchange 的配置问题
def bubble_sort(alist):
    exchange = True
    length = len(alist) - 1
    while length > 0 and exchange:
        exchange = False
        for index in range(0, length):
            if alist[index] > alist[index + 1] and index + 1 <= len(alist) - 1:
                alist[index], alist[index + 1] = alist[index + 1], alist[index]
                exchange = True
        length -= 1
