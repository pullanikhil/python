#create a student table with the given data s-name ,s-rollno,s-age,s-marks
import os
import pickle
os.getcwd()
os.chdir("C:\\Users\\Nikhil\PycharmProjects\pythonProject\\venv")
std_data= open("C:\\Users\\Nikhil\PycharmProjects\pythonProject\\venv\std_data.txt","w+")
std_data.write("s_name\t s_roll\t s_age\t s_marks")
my_list=[]
while True:
     S_name= input("Enter S_name : ")
     my_list.write(str)

     S_roll=int(input("Enter S_roll : "))
     my_list.append(S_roll)

     S_age=int(input("Enter s_age  : "))
     my_list.append(S_age)

     S_marks=float(input("Enter S_marks: "))
     my_list.append(S_marks)
     std_data.write(str(my_list))
     C=input("do you want to add more data[y/n] : ")
     if C=="y":
          continue
     else:
          break
