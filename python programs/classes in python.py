# class myclass:
#     mynum=100
#     def __init__(self,fname,lname,age):
#         self.name=fname
#         self.nname=lname
#         self.age=age
#         print(fname,lname,age)

#     def show(self):
#         print(self.name,self.nname,self.age)
#         print(self.mynum+1)
        

# p1=myclass("ayush","chaurasia",21)
# p2=myclass("anish","chaurasia",22)
# p1.show()            this and lower satement both are same, self is same as instance of that class
# myclass.show(p2) 


# <---------------------inheritance---------------------->

# class phone:
#     def __init__(self,brand,name,price):
#         self.brand=brand
#         self.name=name
#         self.price=price
    
#     def fullname(self):
#         return self.name
# <-----------------accessing base class init method ----------------------->
# class smartphone(phone):
#     def __init__(self, brand, name, price,ram):
#         # super().__init__(brand, name, price)    with the help of super we can call init method of base class and in super class we dont use self 
#         # phone.__init__(self,brand,name,price)  we can also call base class init method with these statement also
#         self.ram=ram

# p1=smartphone("realme","narzo",10000,4)
# print(p1.fullname())

