class Student:
    studentId = str()
    firstName = str()
    middleName = str()
    lastName = str()
    course = str()
    year = int()
    section = str()

    def setInfo(self, si, fn, mn, ln, c, y, s):
        self.studentID = si
        self.firstName = fn
        self.middleName = mn
        self.lastName = ln
        self.course = c
        self.year = y
        self.section = s

    def getInfo(self):
        print(f"Student ID: {self.studentID}")
        print(f"First Name: {self.firstName}")
        print(f"Middle Name: {self.middleName}")
        print(f"Last Name: {self.lastName}")
        print(f"Course Year and Section: {self.course} {self.year}-{self.section}")

stud = Student()
si = input("Student ID: ")
fn = input("First name: ")
mn = input("Middle name: ")
ln = input("Last name: ")
c = input("Course: ")
y = int(input("Year: "))
s = input("Section: ")

stud.setInfo(si, fn, mn, ln, c, y, s)
stud.getInfo()

if y < 1:
    print("Freshmen")
elif y <= 4:
    print("Sophomore")
else:
    print("Invalid Year!")

