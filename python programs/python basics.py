# a=["ayush",1,2,"anish"]
# for i in a:
#     print(i,type(i))


# a,b=map(list,input().split())
# print(a,b)

# a=()
# print(type(a))

# a="ayush chaurasia"
# print(a.title())
# print(a.upper())

# a,b=map(list,input().split())
# print(a,b)
# for i in b:
#     if i in a:
#         a.remove(i)
# str1=" "
# # str1=str1.join(a)
# # print(type(str1))
# for i in a:
#     str1+=i
# print(str1)
# print(1/2) 0
# print(1//2)   0.5

# print("hello",1,"ayush")

# n=int(input())
# a=list(input().split())
# print(n,a)

# print("enter the elements ")
# n=int(input())
# a=list(map(int,input().split()))
# print(a)

# <-------------------------loops in python------------------------------>



# for i in range(10)[::-1]: 9 8 7 6 5 4 3 2 1 0
#     print(i,end=" ")

# for i in range(10,-1,-2):
#     print(i,end= " ")

# for i in reversed(range(10)):
#     print(i,end=" ")

# a=[1,2,3,4]
# b=a
# b[0]=5
# print(a)
# a=[1,2,3,4,5,6]
# for i in range(len(a))[::-1]:
#     print(a[i],end= " ")

# for i in range(len(a)-1,-1,-1):
#     print(a[i],end= " ")

# a=list(map(int,input().split()))
# print(a)

# <-----------------------dictionary--------------------------->
# a={}
# for i in range(2):
#     a1,b=input().split()
#     a[a1]=b
# print(a)
# for i,j in a.items():
#     print(i,j)


# <-------------------------------list comprehension----------------------->

# a=[i**2 for i in range(1,11)]
# print(a)

# a=[[0 for i in range(3)] for i in range(3)]
# for i in range(3):
#     for j in range(3):
#         a[i][j]=int(input())
# print(a)


# <---------------------------functions-------------------->


# def square(a,b):
#     return a*b
# a,b=map(int,input().split())

# print(square(a,b))

# def fact(a):
#     if(a==0 or a==1):
#         return 1
#     return a*fact(a-1)

# a=int(input())
# print(fact(a))

# <----------------passing a list to functions----------------->


# def prn(b):
#     for i in range(len(b)):
#         print(b[i])
#         b[i]=i

# a=list(map(int,input().split()))
# prn(a[::-1])
# print(a)

# a="ayush"
# print(a[:])

# <---------------passing arbitrary values------------------->

# def dishes(*toppings):
#     for i in toppings:
#         print(i)
#     print(type(toppings))

# dishes("cherry","apple","orange")


# def dicti(**details):
#     print(type(details))
#     for i,j in details.items():
#         print(i,j)

# dicti(first_name="ayush",second_name="chaurasia")


# <------------------------lambda function----------------->

# x=lambda a,b:a**b
# print(x(10,2))

# <---------------------sets in pythpn---------------->

# a=set()
# for i in range(3):
#     v=int(input())
#     a.add(v)
# print(a)

# for i in a:
#     print(i)


a=map(str,input().split())
print(list(a))