# # import random
# # n=11
# # list_of_numbers=[]
# # final_list=[]
# # rows=[]
# # colomns=[]


# # def check(a):
# #     for k in final_list:
# #         chk1=[]
# #         chk2=[]
# #         x=k[0]
# #         y=k[1]
# #         for i in range(n):
# #             for j in range(n):
# #                 if i==j:
# #                    if [x+i,y+j] in final_list:
# #                         return 0
# #                    if [x-i,y-j] in final_list:
# #                        return 0
# #                 elif [x+i,y+j] in final_list:
# #                     chk1.append([x+i,y+j])
# #                     if len(chk1)>2:
# #                         return 0
# #                 elif [x-i,y-j] in final_list:
# #                     chk2.append([x-i,y-j])
# #                     if len(chk2)>2:
# #                         return 0

# # for i in range(n):
# #         list_of_numbers.append(i)            
# # def number_generator():
# #     while(1):
# #         r = random.choice(list_of_numbers)
# #         c = random.choice(list_of_numbers)
# #         if r not in rows and c not in colomns:
# #             rows.append(r)
# #             colomns.append(c)
# #             final_list.append([c,r])
# #         if len(final_list)==n:
# #             break       
# # number_generator()           
# # while(1):
# #     if not check(1):

# #         final_list=[]
# #         rows=[]
# #         colomns=[]
        
# #         number_generator()
# #     else:
# #         print(final_list)
# #         new_list=[]
# #         for i in final_list:
# #             new_list.append(i[0]*n + (i[1]+1))
# #         new_list.sort()
# #         for i in new_list:
# #             print(i, end=" ")
# #         break



# import os
# import sys


# def xorKey(x, queries):
#     ans = []
#     bitset = [None]*(1 << 16)
#     for i in range(len(x)):
#         if bitset[x[i]]:
#             bitset[x[i]].append(i)
#         else:
#             bitset[x[i]] = [i]
#     m = max(x)
#     i = 0
#     while m > 0:
#         m >>= 1
#         i += 1
#     m = (1 << i) - 1
#     allset = ((1 << 16) - 1) & m
    
#     for q in queries:
#         ideal = q[0]^allset
#         for i in range(1 << 16):
#             if inrange(bitset[i^ideal], q):
#                 ans.append(allset^i)
#                 break
#     return ans


# def inrange(a, q):
#     if a:
#         p = b_search(a, q[1]-1)
#         if p < len(a) and a[p] < q[2]:
#             return True
#         return False
#     return False


# def b_search(a, x):
#     l = 0
#     r = len(a)
#     while l != r:
#         m = l + (r-l)//2
#         if x > a[m]:
#             l = m + 1
#         else:
#             r = m
#     return r

# if __name__ == '__main__':
   

#     t = int(input())

#     for t_itr in range(t):
#         nq = input().split()

#         n = int(nq[0])

#         q = int(nq[1])

#         x = list(map(int, input().rstrip().split()))

#         queries = []

#         for _ in range(q):
#             queries.append(list(map(int, input().rstrip().split())))

#         # result = xorKey(x, queries)



n=int(input())
a=list(map(int,input().split()))
b=a[:]
b.sort()
for i in range(n)

       