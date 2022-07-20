


class Person:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name



class Employee(Person):
    def __init__(self, first_name, last_name, job_title):
        super(Employee, self).__init__(first_name, last_name)
        self.job_title = job_title



# create an instance of class Employee with your personel information
Employee1=Employee("Kerem","Demir","intern")
# print out fname, lname and job_title using same instance

print(Employee1.fname)
print(Employee1.lname)
print(Employee1.job_title)