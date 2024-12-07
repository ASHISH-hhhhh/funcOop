def sum(a,b):
    return a+b
add=sum(1,10)
print(add)
def average_three(a,b,c):
    av=(a+b+b)/3
    return av
av=average_three(1,1111,11111)
print(av)
def calc_prod(a=1,b=11):
    return a*b
prod=calc_prod(100)
print(prod)

list=[1,2,3,4,5,6,7,8,9]
def len_list(l1):
    if(type(l1)==type([1,2])):
        return len(l1)
    else:
        return "Input is not a List"
lenList=len_list([1,2,3,4,5,6,7,8,9,10,11])
print(lenList)
# Printing Listing
print("++++++++++PRINTING LIST+++++++++++")
def prin_list(l1):
    for el in range(0,len(l1)):
        print(l1[el],end=" ")
prin_list([1,2,3,4,5,6,7,8,9,10,11])
print("\n")
def factorial(a):
    facto=1
    for i in range(1,a+1):
        # print(i)
        facto=facto*i
    return facto
print(factorial(6))
def d_to_iRupee(d1):
    return d1*84
print(d_to_iRupee(1000))

print("+++++OOPS in python+++++")

class Student:
    def __init__(self,fullName,nickName):
        print("Executing the __init__ function")
        self.FullName=fullName
        self.NickName=nickName

s1=Student("Ashish Biradar","The Hindu")
print(s1.FullName)
print(s1.NickName)
s2=Student("Nate","Diaz")
print(s2.FullName)
print(s2.NickName)    

print(s1.FullName,s1.NickName)
s2.FullName="Nick"
print(s2.FullName,s2.NickName)

class Car():
    def __init__(self,color,brand):
        print("Here Confrimation",self)
        self.Color=color
        self.Brand=brand
c1=Car("Matt Dark Red","Jaguar")
print("Here confirmation",c1)
print(c1.Color,c1.Brand)
    
class CollegeStudents:
    collegename="Biradars Institute of Technology"
    def __init__(self,name,surname,branch,year,gender):
        self.name=name
        self.surname=surname
        self.branch=branch
        self.year=year
        self.gender=gender

    def studentSummary(self):
        print(self.name," ",self.surname," is a student of ",self.collegename," in the branch of ",self.branch," studying in ",self.year," year ")

student21=CollegeStudents("Ashish","Biradar","CSE","1st","Male")
student21.studentSummary()
print(student21.collegename)

class StudentAverage():
    college_name="Biradars Institute of Technology"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in range(0,len(self.marks)):
            sum=sum+self.marks[i]
        return sum/len(self.marks)
    
student21=StudentAverage("Ashish Biradar",[96,93,89,56,97,87,99])
print(student21.college_name)
print(student21.name)
print(student21.marks)
print(student21.name[0:7],"Your average marks are ",student21.average())

print("After learning/revising the git commit command")


print("After learning/revising the git commit command for git diff only")

def algo():
    print("Hello from algo ji")

algo()