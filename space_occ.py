def size_r(path):
    size = 0
    arr = os.listdir(path)
    for x in range(len(arr)):
        if os.path.isfile (path + "/" + arr[x]):
           size = size + os.stat(path + "/" + arr[x]).st_size
        else:
            path_x = path + "/" + arr[x]
            size += size_r(path_x)
    return size


import os
full_path = input("give path:")

size =size_r(full_path)

print(size)