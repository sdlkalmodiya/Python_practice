arr1 = [-3, 6, 8, -3, 7, 100, 120, 100, 7, -300]

arr_neg = [i for i in arr1 if i < 0]
arr_pos = [i for i in arr1 if i >= 0]

arr1 = arr_neg + arr_pos

print(arr_neg, "\n", arr_pos, "\n", arr1)
