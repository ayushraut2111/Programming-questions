# def solve(n,k,s):
    count=0
    # if len(set(s))==1 and k==2:
    #     return 1
    while len(s)>1:
        for i in range(0,n-1):
            for j in range(i+1,n):
                st=set(s[i:j])
                if len(st)==k:
                    s=s[:i]+s[j:]
                    print(s)
            count+=1
    return count



# for _ in range(int(input())):
#     n=int(input())
#     k=int(input())
#     s=input()
#     print(solve(n,k,s))
    
# s=[i for i in "xbawtvebluuagttbeqbihnlucpmg" ]
# d={}
# res=0
# left=right=0
# while(right<len(s)):
#     r=s[right]
#     if(r in d):
#         if(d[r]<left):
#             d[r]=right
#             right+=1
#         else:
#             res=max(res,right-left)
#             left=d[r]+1
#             d[r]=right
#             right+=1      
#     else:
#         d[r]=right
#         right+=1
# print(max(res,right-left))

# def isPrime(n):
#     count=0
#     for i in range(1,n):
#         if(n%i==0):
#             count+=1
#     if(count>2): 
#         return False
#     return True
    
# [print(i,end=",") for i in range(1,20) if isPrime(i)]

# def Tuple(tuple, t):
#     val = 0
#     for tup in tuple:
#         if (tup == t):
#             val = val + 1
#         elif(tup&t):
#             val = val+2
#         else:
#             return val
#     print(tuple)
# tuple = (1,1,2,2,5)
# def multiply_5(val):
#     return val * 5
# def addition_5(val):
#     return val+5
# def sub_5(val):
#     return val-5
# print(Tuple)
# Tuple_1 = [1,2,3,4,5]
# Tuple_2 = [5,10,15,20,25]
# Tuple = set(Tuple_1)&set(Tuple_2)
# list(map(lambda val:val*5, Tuple_1))
# print(Tuple)

name1 = [
   ['Alice','Bob','Ben','Mark'],
    ['Smith', 'Jones', 'White']
    ]
import copy
name2 = copy.deepcopy(name1)
name3 = name1.copy()
name2[1][2] = 'Johnson'
for idx,val in enumerate(name1):
    temp=(idx, val)
print(temp)   
name1.pop()
print(name1)
print(name2)
print(name3)