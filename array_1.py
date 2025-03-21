# print max no to the right of each element, if not present then print -1 with it

nums1 = [2,777,-10,3,8,100,103,7]

left = 0
right = 1

while left<len(nums1):
    if right==len(nums1):
        print(nums1[left], -1)
        left += 1
        right = left + 1
    elif nums1[left]<nums1[right]:
        print(nums1[left], nums1[right])
        left+=1
        right=left+1

    else:
        right+=1


# o/p:-
# 2 777
# 777 -1
# -10 3
# 3 8
# 8 100
# 100 103
# 103 -1
# 7 -1
