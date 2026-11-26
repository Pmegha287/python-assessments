class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def hello():
        print("Hello!")

Student.show_school()
Student.hello()