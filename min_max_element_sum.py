# method:-1 using for loop

arr1 = [-3, 6, 8, -10, 7, 100]

min_num = arr1[0]
max_num = arr1[0]

for i in arr1:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
        
print("max = ", max_num, " min = ", min_num)
print("sum = ", max_num+min_num)

# method:-2 using min and max function 

arr1 = [-3, 6, 8, -10, 7, 100]

print("sum = ", max(arr1)+min(arr1))
