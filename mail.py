#to create a login system using python file handling
#text file is named data.txt
#regular expressions is used to validate email and password


import re
def validation(a,b):
    user='^\A[a-z][a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-z]{2,3}$'
    pwd="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    db1=open('data.txt','a')
    if re.search(user,a):
        if re.search(pwd,b):
            db1.write(a+","+b+"\n")
            db1.close()
            print("Registration Successfull..!")
        else:
            print("Kindly enter a valid Password..!")
    else:
        print("Kindly enter a valid Username..!")
def new_id(a,b,c):
    db=open("data.txt",'r')
    for i in db:
        x,y=i.split(",")
        if x==a:
            print("Username already exists..!")
            print("Kindly enter a new Username.")
            break
    else:
        if b==c:
            validation(a,b)
def register():
    a=input("Create Username : ")
    b=input("Create Password : ")
    c=input("Confirm Password : ")
    new_id(a,b,c)
def forgot_pwd(x,y):
    n=int(input("Enter your choice : "))
    if n==1:
        login()
    elif n==2:
        m=input("Enter your Username : ")
        if m==x:
            print("Your Password : ",y)
        else:
            print("Username incorrect..!")
    else:
        print("Invalid input..!")
def verify(username,password):
    dbl=open("data.txt","r")
    for i in dbl:
        x,y=i.split(",")
        y=y.strip()
        if x==username:
            if y==password:
                print("Login Success")
            else:
                print("""
                    1)Try again.
                    2)Forget password.
                """)
                forgot_pwd(x,y)
                break
    else:
        print("Username is not found. Kindly Register.")
def login():
    username=input("Enter your Username : ")
    password=input("Enter your Password : ")
    verify(username,password)
def home():
    while True:
        entry=input("Login|Register : ")
        if entry=="Login":
            login()
        elif entry=="Register":
            register()
        else:
            print("Invalid Input..!")
            break
home()
