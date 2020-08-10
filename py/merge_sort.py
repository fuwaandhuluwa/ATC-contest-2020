# encoding=utf-8
#  python heap sort is very low, so we will implement merge sort algorithm to improve performance for large data set
#  A small amount of data quick sort is better ()
#  Timsort 是结合了合并排序（merge sort）和插入排序（insertion sort）而得出的排序算法，它在现实中有很好的效率。
#  Timsort is the direction of next step optimization

import numpy as np

from py.Point import Point


def merge(arr, l , m ,r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组
    left = np.ndarray([1, n1], dtype=Point)[0]
    right = np.ndarray([1, n2], dtype=Point)[0]

    # copy 数据到临时的数组
    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]

    # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 拷贝 left[] 的保留元素
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    # 拷贝 right[] 的保留元素
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):  # l: left index; r: right index
    if l < r:
        m = int((l+(r-1))/2)
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("给定的数组")
# for i in range(n):
#     print("%d" % arr[i]),
#
# merge_sort(arr, 0, n - 1)
# print("\n\n排序后的数组")
# for i in range(n):
#     print("%d" % arr[i])