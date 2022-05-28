#!/usr/bin/python
arr = [-2, 0, 11, -9, 45]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        first = arr[i]
        second = arr[j]
        if first > second:
            arr[i] = second
            arr[j] = first

print("Sorted array is", arr)
