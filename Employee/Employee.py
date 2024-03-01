class Employee:
    fname = str()
    mname = str()
    lname = str()
    emp_id = str()
    age = int()
    sex = str()
    address = str()
    civil_status = str()
    employment_status = str()

    def employeeInfo(self, eid, fn, mn, ln, a, s, add, cs,es):
        self.lname = ln
        self.mname = mn
        self.fname = fn
        self.age = a
        self.address = add
        self.civil_status = cs
        self.emp_id = eid
        self.sex = s
        self.employment_status = es
    def getlname(self):
        return self.lname
    def getfname(self):
        return self.fname
    def getmname(self):
        return self.mname
    def getage(self):
        return self.age
    def getaddress(self):
        return self.address
    def getcivil_status(self):
        return self.civil_status
    def getemp_id(self):
        return self.emp_id
    def getsex(self):
        return self.sex
    def getemployment_status(self):
        return self.employment_status

jane = Employee()
eid = (input("Employee ID: "))
fn = input("Enter first name: ")
mn = input("Enter middle name: ")
ln = input("Enter last name: ")
a = int(input("Enter age: "))
add = input("Enter Address: ")
cs = input("Enter Civil Status: ")
s = input("Enter sex: ")
es = input("Enter Employment Status: ")

jane.employeeInfo(eid, fn, mn, ln, a, s, add, cs, es)
print(f"Employee ID: {jane.getemp_id()}")
print(f"Employee Name: {jane.getfname()} {jane.getmname()} {jane.getlname()}")
print(f"Age: {jane.getage()}")
print(f"Adrress: {jane.getaddress()}")
print(f"Civil Status: {jane.getcivil_status()}")
print(f"Sex is: {jane.getsex()}")
print(f"Employment Status: {jane.getemployment_status()}")




