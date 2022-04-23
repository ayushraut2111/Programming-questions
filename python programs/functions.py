# def sum(a,b):
#     return a+b

# a=int(input())
# b=int(input())
# print(sum(a,b))

# def allsum(a):
#     b=int(0)
#     for i in a:
#         b=b+i
#     print(type(a))
#     return b
# a=[i for i in range(10)]
# b=allsum(a)
# print(b)


# def array(*a):
#     print(a)
#     print(type(a))

# array(1,2,2,3,3,)

# def dict(a):
#     for key,value in a.items():
#         print(key,value,end='\n')
# s={'1':'2','2':4}
# dict(s)
def dict(**a):
    return a
if __name__=="__main__":
    a=dict(name='ayush', gh='jk')
    print(a)