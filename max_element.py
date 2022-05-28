#!/usr/bin/python
arr = [1, 2, 3, 4, 5]

if len(arr) == 0:
  print ("there is no maximum")
else:
    max_array = arr[0]
    if len(arr) > 1:
        for i in range(1, len(arr)):
            if max_array < arr[i]:
                max_array = arr[i]
    print ("max value is", max_array)


