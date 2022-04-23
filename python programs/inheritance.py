# class a:
#     def function1(self):
#         print("hello i am function 1")
# class b(a):
#     def function2(self):
#         print("hello i am function 2")
# class c(b):                              
#     def function3(self):
#         print("hello i am function 2")

# a1=c()
# a1.function1()


class a:
    def __init__(self):
        print("in init a")

    def function1(self):
        print("hello i am function 1")

class c:
    def __init__(self):
        super().__init__()
        print("in init c")

    def function3(self):
        print("hello i am function 3")


class b(c,a):
    def __init__(self):
        super().__init__()
        print("in init b")
        c.function3()

    def function2(self):
        print("hello i am function 2")


a1=b()
