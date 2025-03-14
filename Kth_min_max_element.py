k = int(input("enter the value of k:- "))
arr1 = [-3, 6, 8, -10, 7, 100, 120, -300]

arr1.sort()
print(arr1)
k_min = arr1[k-1]
k_max = arr1[-k]
print(f"{k}th min element:- ", k_min)
print(f"{k}th max element:- ", k_max)
