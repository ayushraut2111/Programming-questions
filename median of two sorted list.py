from math import floor


nums0 = [1, 2, 5]
nums1 = [3, 6, 7]
l=nums0+nums1
l.sort()
print(l)
ans=floor(len(l) / 2)
print(l[ans])