'''
class Student:
    stud_id = str()
    fname = str()
    mname = str()
    lname = str()
    course = str()
    year = int()
    section = str()

    def setInfo(self, si, fn, mn, ln, c, y, s):
        self.stud_id = si
        self.fname = fn
        self.mname = mn
        self.lname = ln
        self.course = c
        self.year = y
        self.section = s

    def getstud_id(self):
        return self.stud_id

    def getfname(self):
        return self.fname

    def getmname(self):
        return self.mname

    def getlname(self):
        return self.lname

    def getcourse(self):
        return self.course

    def getyear(self):
        return self.year

    def getsection(self):
        return self.section

    def getInfo(self):
        print(f"Student ID: {stud.getstud_id()}")
        print(f"First Name: {stud.getfname()}")
        print(f"Middle Name: {stud.getmname()}")
        print(f"Last Name: {stud.getlname()}")
        print(f"Course Year and Section: {stud.getcourse()} {stud.getyear()}-{stud.getsection()}")

stud = Student()
si = input("Student ID: ")
fn = input("First name: ")
mn = input("Middle name: ")
ln = input("Last name: ")
c = input("Course: ")
y = int(input("Year: "))
s = input("Section: ")

stud.studentInfo(si, fn, mn, ln, c, y, s)
getInfo()
if int(y) < 1:
    print("Freshmen")
elif int(stud.year) <= 4:
    print("Sophomore")
else:
    print("Invalid Year!")
'''







