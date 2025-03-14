k = int(input("enter the value of k:- "))
arr1 = [-3, 6, 8, -10, 7, 100, 120, -300]

arr1.sort()
print(arr1)
k_min = arr1[k-1]
k_max = arr1[-k]
print(f"{k}th min element:- ", k_min)
print(f"{k}th max element:- ", k_max)



# if list contains duplicates 

k = int(input("enter the value of k:- "))
arr1 = [-3, 6, 8, -3, 7, 100, 120,100,7, -300]

arr2 = []

for i in arr1:
    if i not in arr2:
        arr2.append(i)
 
arr2.sort()
print("min_num", arr2[k-1], "\n", "max_num", arr2[-k])
