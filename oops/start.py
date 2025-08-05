# class Car : 
#     color = "blue"
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model


# car1 = Car("Buggati", "sd41asd")


# print(car1.model,car1.name)

# class Student : 
#     def __init__(self,name,java, python,node):
#         self.name = name
#         self.python = python
#         self.java = java
#         self.node = node
#     def getMark(self) : 
#         print(self.java + self.python + self.node / 3)


# stuent1 = Student("Abir",5,4,5)

# stuent1.getMark()

# class Account : 
#     def __init__(self,bal, acc):
#         self.blance = bal
#         self.account_no = acc

#     def Dibit (self,deposit) :
#         self.blance += deposit 

#     def Credit(self, wihtdrow) : 
#         self.blance -= wihtdrow


# acc1 = Account(5000,456465) 

# acc1.Dibit(50)

# acc1.Credit(150)

# print(acc1.blance)


# practice 1 

# class Circle():
#     def __init__(self,r):
#        self.redius = r
    
#     def area(self):
#       return  3.14159 * self.redius **2
#     def perimeter(self):
#        return 2* 3.141 * self.redius 

# c1 = Circle(21)

# print(c1.area())
# print(c1.perimeter())

# practice 2 

# class Employee():
#     def __init__(self,role,department,salary):
#        self.role = role 
#        self.department = department
#        self.salary = salary
      
#     def showDetails(self) :
#         print("Role :" , self.role)
#         print("Department :" , self.department)
#         print("Salary :" , self.salary)

# class Engineer(Employee):
#     def __init__(self,age,name):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "Java", "60000")


# en1 = Engineer(45,"Arif biswas")

# en1.showDetails()

class Order():
    def __init__(self,item, price):
        self.item = item
        self.price = price
    
    def __gt__(self,ord):
        return self.price > ord.price
    # def __lg__(self,ord) :
    #     return self.price < ord.price

ord1 = Order("KOla",12)
ord2 = Order("Apple",16)

print(ord1 > ord2)