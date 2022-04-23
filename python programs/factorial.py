def factorial(a):
    # print(type(a))
    if a==0 or a==1:
        return 1
    f=a*factorial(a-1)
    return f
if __name__=="__main__":
    print(factorial(5))
