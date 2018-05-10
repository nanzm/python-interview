class Student():
    name = ""
    age = 0

    def __init__(self):
        print("初始化")

    def print_file(self):
        print("name:" + self.name)
        print("age:" + str(self.age))


student = Student()
student.print_file()
