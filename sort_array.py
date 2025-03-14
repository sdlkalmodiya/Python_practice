# sort an array containing 0s, 1s,and 2s without inbuilt methods

arr1 = [2,1,2,0,1,2,0,1,0]

count_0 = 0
count_1 = 0
count_2 = 0

for i in arr1:
    if i==0:
        count_0 += 1
    elif i==1:
        count_1 += 1
    elif i==2:
        count_2 += 1
        
arr2=[]
for j in range(count_0):
    arr2.append(0)

for j in range(count_1):
    arr2.append(1)

for j in range(count_2):
    arr2.append(2)
    
print(arr2)
