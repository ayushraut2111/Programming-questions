strs = ["green", "blue", "red", "red"]
# mp={}
# for i in strs:
#     if i not in mp:
#         mp[i]=1
#     else:
#         mp[i]+=1
# for key,value in mp.items():
# l1=["red" for i in range(mp['red'])]
# l2=["green" for i in range(mp['green'])]
# l3=["blue" for i in range(mp['blue'])]
# ans=l1+l2+l3
# print(ans)
ans=[]
red=strs.count('red')
if red>0:
    ans=['red' for i in range(red)]
green=strs.count('green')
if green>0:
    ans=ans+['green' for i in range(green)]
blue=strs.count('blue')
if blue>0:
    ans=ans+['blue' for i in range(blue)]
print(ans)

