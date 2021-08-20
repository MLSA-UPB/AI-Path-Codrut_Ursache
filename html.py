import numpy as np

arr, cacat = []
arr.append([1, 2, 3, 4])
arr.append([5, 6, 7, 8, 9])
np_arr = np.array(arr)
print(np_arr)
for item in np_arr:
    print(item[0])
