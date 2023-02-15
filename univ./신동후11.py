class Employee:
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    def getSalary(self):
        print("{}'s salary is {}".format(self.name, self.salary))

    def getCount(self):
        print("Total employee count: ", Employee.count)


kim=Employee("kim", 2000)
kim.getSalary()
kim.getCount()
lee=Employee("lee", 3000)
lee.getSalary()
lee.getCount()