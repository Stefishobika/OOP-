#STEFI SHOBIKA SUKUMAR URK24CS1067

class Human():
    def __init__(self,name,aadharcardnum,dob):
        self.name=name 
        self.aadhar=aadharcardnum
        self.dob=dob
    def show(self):
        print("NAME:",self.name,"AADHAR NUM:",self.aadharcardnum,"DOB:",self.dob)
class student(Human):
    def __init__(self,name,aadharcardnum,dob,d,c,a):
        super.__init__(name,aadharcardnum,dob)
        self.attendance=a
        self.cgpa=c
        self.dept=d
    def show(self):
        super.show()
        print("DEPARTMENT:",self.dept,"ATTENDANCE:",self.attendance,"CGPA:",self.cgpa)
s=student("Dany","7483420394036","30-06-2007","91%","8.84","CSE")
s.show()
