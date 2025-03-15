arr1 = [-3, 6, 8, -3, 7, 100, 0, 120, 100, 7, -300]

arr2 = [6, -4, 0, -3, 100, -5]

arr1.sort()
arr2.sort()

arr_intersection = list(set(arr1) & set(arr2))

arr_union = list(set(arr1) | set(arr2))
print(arr_intersection, "\n", arr_union)
