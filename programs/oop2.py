

class Employee:
    # constructor : constructor is invoked automatically when object is created 
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def displayInfo(self):
        print("Employee name :", self.name)
        print("Employee age  :", self.age)
        print("Employee city:", self.city)


emp1 = Employee("rita",28,"Hyd")
emp1.displayInfo()

emp2 = Employee("rao",28,"chennai")
emp2.displayInfo()

emp3 = Employee("raju",28,"bangalore")
emp3.displayInfo()
