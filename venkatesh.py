'''age=int(input("enter the age:"))
if age >= 18:
    print("ready for vote")
else:
    print("not reday for vote")'''
'''marks=int(input("enter the students marks:"))
if marks >=40:
    print("Pass")
else:
    print("Fail")'''
'''number =int(input("enter the numbers:"))
if number %2==0:
    print("even")
else:
    print("odd")'''
'''number =int(input("enter the numbers:"))
if number <= 0:
    print("negative number")
elif number  >= 0:
    print("postive number")
else:
    print("zero")'''
'''n1=int(input("enter the n1:"))
n2=int(input("enter the n2:"))
n3=int(input("enter the n3:"))
if n1>n2 and n3:
    print("n1 is greater than all")
elif n2>n1 and n3:
    print("n2 is greater than all")
else:
    print("n3 is greater than all")'''
'''marks =int(input("enter the marks:"))

if marks>=90 and marks<= 100:
    print("a grade")
elif marks >=80 and marks<= 89:
    print("b grade")
elif marks >=70 and marks<= 79:
    print("c grade")
elif marks >=60 and marks<= 69:
    print("d grade")
elif marks >=50 and marks<= 59:
    print("e grade")
elif marks >=40 and marks<= 49:
    print("pass")
else:
    ("fail")'''
'''balance = 10000
pin = 1234
user_pin = int(input("enter the pin:"))
if pin == user_pin:
    withdraw =int(input("enter the withdraw amount:"))
    if(withdraw  > balance):
        print("insufficent funds")
    else:
        if(withdraw_amount%500 == 0 and withdraw_amount%100 == 0):
            print("withdraw sucess")
        else:
            print("enter valid amount 100 's and 500's only")
            print("withdraw sucess")
            remaining-balance==balance-withdraw
            print("remaing balance:",remaining-balance)
       
else:
    print("invalid pin:")'''
'''p= int(input().strip())
s = int(input().strip())
power_increased =p<< s
print(power_increased)'''
'''user = "venkatesh"
pin = 1234
user=input("enter the name:")
password=int(input("enter the password:"))
if user ==user  and pin == pin:
    print("login")
elif(pin != password):
    print("enter valid password")
else:
    print("failed")'''
'''for i in range(1,8,6):
    print(i)'''
'''for i in range(1,4):
    print("class",i)
    for i in range(1,3):
        print("section:",i)'''
'''j=5
for i in range(1,11):
    print(j,"x", i ,  "=" ,  j * i)'''
'''j=int(input())
for i in range(1,11):
    print(j, "x", i, "=", j*i)'''
'''name ="venkatesh"
print(name[-1])'''
'''l = [10,20,30]
for a in l:
    print(a)'''
'''i = 1
while i <  6:
    print(i)
    i += 1'''
'''i = 100
while i >= 5:
    print(i)
    i -= 5
i = 1
count = 0
while i <= 10:
    count += 1
    i += 1
    print("count:",count)'''
'''sum = 1
for i in range (1,11):
    sum *= i 
    print(sum)'''
''''i = 1
sum = 1
while i <= 10:
    sum += 1
    i+=1
    print(sum)
sum = 0
for i in range (0,11,2):
    sum += i 
    print(sum)
    
i = 1
sum = 0
while i <= 10:
    sum += i
    i+=2
    print(sum)'''
'''i = 0
while i <=10:
    if(i%2 != 0):
        continue
    print(i)'''
'''i = 1
while i <=10:
    print(i**2)
    i+=1'''
'''name ="venkatesh"
v = "aeiouAEIOU"
while v in name :
    if  v in name:
        print("vowel")
    else:
        print("not")
n = int(input())
a = int(input())
b = int(input()) 
for i in range(1,n+1):
    if(i % a ==  0  or  i%b==0):
            print(i)
print(2%2)'''
'''from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
# Dataset
weather = ['Sunny', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Sunny', 'Rainy']
# Target class
buys_computer = ['Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes']
# Convert categorical data into numbers
encoder_weather = LabelEncoder()
encoder_target = LabelEncoder()
X = encoder_weather.fit_transform(weather)
y = encoder_target.fit_transform(buys_computer)
# Convert X into 2D format
X = X.reshape(-1, 1)
# Create Naive Bayes model
model = GaussianNB()
# Train the model
model.fit(X, y)
# New data
new_weather = ['Sunny']
# Convert new data into numbers
new_X = encoder_weather.transform(new_weather)
new_X = new_X.reshape(-1, 1)
# Prediction
prediction = model.predict(new_X)
# Probability of each class
probability = model.predict_proba(new_X)
# Display results
print("Training Data:")
print("__________________________________")
for i in range(len(weather)):
    print(weather[i], "->", buys_computer[i])
print("==================================")
print("\nNew Data:", new_weather[0])
print("__________________________________")
print("Predicted Class:", encoder_target.inverse_transform(prediction)[0])
print("\nClass Probabilities:")
print("=================================")
for class_name, prob in zip(encoder_target.classes_, probability[0]):
    print(class_name, ":", round(prob, 4)) '''
'''i=1
while(i<=10):
    if i==5:
        continue
    elif i==3:
        pass
    print(i)
    i+=1'''
'''n = 1,2,3,4
print(n[-1:-3])'''

'''num=int(input())
sum=0
while num>0:
    d=num%10
    sum+=d
    num//=10
print(sum)'''
'''num=int(input())
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num//=10
print(rev)'''
'''num=int(input())
n=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num//=10
print(rev)
if n == rev:
    print("palindrome")
else:
    print("not")'''
'''n = 12345689
l = 0
s = 9
while n > 0:
    d = n % 10
    if d> l:
        l = d
    if d<s:
        s = d
    n //= 10
print("largest number is;",l)
print("smallest number is;",s)
print("difference largest number and smallest number: ",l -s)'''
'''n = int(input())
e = 0
o = 0
while n > 0:
    d = n % 10
    if d %2 == 0:
        e+=1 
    if d % 1== 0:
        o +=1
        n //= 10
print("even  number is;",e)
print(" odd number is;",o)'''
#check prime number
"""count =0
n = int(input())
for i in range(1,11):
     if n % i == 0 :
         count += 1
    if count == 2:
             print("prime number " )
   else:
             print("not prime")"""
#strings
'''n ="gangadhar "
print(n.upper())

n1="""vedhanth sai
venkatesh"""
print(n1.capitalize())'''
'''
n="reddy VENKATESH"
print(n.swapcase())

n="kesava"
print(n)
print(n.replace("kesava","HOD"))
'''

"""n="siva                                                                                                            "
print(len(n))
print(len(n.strip()))
"""
'''print("anuty anuty dim dim ro dim dim rooo".count("dim"))'''

'''n="reddy"
print(n.find("d"))


n1="vedhanth sai"
print(n1.rfind("a"))
'''
#formating string
'''n=20.34734
print(f"{n:.0f}")'''
#index
'''n = "venkatesh"
print(n.find("e"))'''
#split
'''n = "venkatesh"
print(n.split("a"))'''
'''n = ["10","20","30","40"]
print(" ".join (n))'''
# strat switch
'''n ="rohit"
print(n.start switch("r"))'''
"""n ="rohit"
print(n.isalpha())
#isalpha
n ="venkatesh"
print(n.isdigit())"""
"""n ="venkatesh"
print(n.isupper())"""
"""n ="venk"
print(n.center(10,"*"))
"""
"""print(chr(65))"""
#without slicing
'''n = "venkatesh"
rev =" "
for i in range(len(n)):
    rev = n [i] + rev
print(rev)'''
'''n = "venkatesh"
print(n[ ::-8])'''
#without count
"""n = "banana"
s = " "
for i in n:
    if i not in s:
        c = 0
        for j in n:
            if i == j :
                c += 1
        print(i,c)
        s+=i"""
"""#Hello world program
print("Hello, World!")


#Variables & Data Types
name = "sudheer"
age = 19
height = 6
student = True
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", student)
print(type(name))
print(type(age))
print(type(height))
print(type(student))
"""

"""#Input, Output & Type Casting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print("Hello! My name is", name)
print("I am", age, "years old.")
print("I live in", city)"""


"""#Operators in Python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)





#Mini Python Project – Student Information Program
name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = float(input("Enter marks: "))
print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)"""
"""l = [10,5,6,3,8]
sum = 0
for i in (len(l)):
    a+=1(i)
average = a/len(l)
print(average)"""

"""num = [1,-10,5,6,-3,2]
for i in num:
    if i>=0:
        print("postive:",i)
    else:print
        print("negative:",i)"""
"""num = [1,-10,5,6,-3,2]
for i in num:
pos_c=+1
    if i>=0:
        pos_c=+1
    else:
print("postive:",i)
print("negative:",i)"""
"""num =[0,5,0,3,2,0,0]
print(num.count(0))"""
"""num =[10,20,90,60,70,80,30]
g=0
for i in num:
    if i>=50:
        print(i)
        g+=1
print("greatest:",g)"""
""" = [0,5,0,3,2,0,0]
for i in range(len(1)):
    if 1[i]==0:
        l[i]=1
print(l) """


'''#Conditional Statements
marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")'''








'''#Loops & Number Patterns
n = int(input("Enter a number: "))

print("Numbers from 1 to N:")
for i in range(1, n + 1):
    print(i, end=" ")

print("\nNumbers from N to 1:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1

print("\nMultiplication Table:")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)'''


"""#Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))


#Scope of Variables
x = 1000

def show_scope():
    y = 500
    print("Local variable:", y)
    print("Global variable:", x)

show_scope()

print("Global variable outside function:", x)"""
"""#Modules & Packages
import math
import random
import datetime

num = 35

print("Square root:", math.sqrt(num))
print("Random number:", random.randint(1, 100))
print("Current date and time:", datetime.datetime.now())"""
"""o=["--x","x++","x++"]
x=0
for i in o:
     if  "+" in i:
         x+=1
     else:
         x-=1
print(x)"""
"""a = [[1,2,3],[6,4,1]]
l = 0
for i in a:
    sum=0
    for j in i:
        sum+=j
    if sum>1:
        l=sum
print(l)"""
'''l =[[1,2,3],
    [4,5,6],
    [7,8,9]]
a = 1
for i in l:
    for j in i:
        a*=j
print(a)'''
"""l =[[1,2,3],
    [4,5,6],
    [7,8,9]]
e= 0
o=0
for i in l:
    for j in i:
        if j % 2 ==0:
            e+=1
            
        elif j%2 !=0:
            o+=1
print(e)
print(o)"""
"""l =[[1,2,3],
    [4,5,6],
    [7,8,9]]
t = 0
for i in l:
    for j in i:
      t +=j
print(j)"""
"""s= 3
Scores= [60,0,80,50,80,0,100,100,0,100,]
matches=len(Scores) //s
heighest_average=0
for i in range(s):
    start=i*s
    e=start+s
    sum=0
    for j in range(start,e):
        sum+=Scores[j]
    if sum//matches>heighest_average:
        heighest_average=sum//matches
print(f{heighest_average,2f})"""
"""nums=[1,2,2,3,3,1]
for i in nums:
     if nums.count (i)>1:
        print("true")
        break
     else:
        print("False")"""
"""nums=[1,2,2,3,3,1]
for i in nums:
     if 0:2(i)>1:
        print("true")
        break
     else:
        print("False")"""
"""nums=[1,2,3,1]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]-nums[j]==0 and i!=j:
            print(True)
            break
else:
        print(False)"""
"""num1=[4,3,2,1],num2=[2,2,5,2,3,6]
for i in nums1:
    if i in nums2:"""



""" #Lists
numbers = [30, 10, 50, 20, 40]
print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
numbers.append(60)
print("After adding 60:", numbers)
numbers[1] = 15
print("After updating second element:", numbers)
numbers.remove(50)
print("After removing 50:", numbers)
numbers.sort()
print("Sorted list:", numbers)"""
"""#Tuples
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Tuple slice:", numbers[1:4])
print("Length of tuple:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 40:", numbers.index(40))
new_tuple = numbers + (60, 70)
print("After concatenation:", new_tuple)"""



"""#Sets
set_a = {10, 20, 30, 40, 40}
set_b = {30, 40, 50, 60}
print("Set A:", set_a)
print("Set B:", set_b)
set_a.add(70)
print("After adding 70:", set_a)
set_a.remove(20)
print("After removing 20:", set_a)
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))
#Dictionaries
student = {
    "Name": "Venkatesh",
    "Age": 19,
    "Course": "B.Tech",
    "City": "Kurnool"
}
print("Name:", student["Name"])
print("Course:", student["Course"])
student["Email"] = "Venkatesh@example.com"
print("After adding Email:", student)
student["Age"] = 22
print("After updating Age:", student)
student.pop("City")
print("After removing City:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Number of details:", len(student))"""
#2465
'''nums =[4,1,4,0,3,5]
s=set()
n=len(nums)//2
for i in range (n):
    a=min(nums)
    b=max(nums)
    average=(a+b)/2
    s.add(average)
    nums.remove(a)
    nums.remove(b)
print(len(s))'''
"""nums =[4,1,4,0,3,5]
n=len(nums)//2
s=set()
nums.sort()
for i in range(n):
    a=(nums[i]+nums[len(nums)-i-1])/2
    s.add(a)
print(len(s))
#1207
a = [1,2,2,1,1,3]
s=set(a)
s1=set()
for i in s:
    s1.add(a.s)
    if len(s) == set(a):
        print("true")
    else:
        print("False")
#1684
"""
"""def  add():
    a = 10
    b = 20
    print(*a+b)
add()"""
'''#File Handling
# Create and write data
with open("student.txt", "w") as file:
    file.write("Name: Venkateswara Reddy\n")
    file.write("Course: CSE-DS\n")
# Read and display data
with open("student.txt", "r") as file:
    print("Original file content:")
    print(file.read())
# Append new data
with open("student.txt", "a") as file:
    file.write("Internship: InternNova\n")
# Display updated content
with open("student.txt", "r") as file:
    print("Updated file content:")
    print(file.read())'''




'''#Exception Handling
# Invalid user input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Error: Please enter a valid number.")
# Division by zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
# File not found
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")'''
'''# Python Libraries
import random
import math
from datetime import datetime
# Random: generate a random number
number = random.randint(1, 100)
print("Random number:", number)
# Math: calculate square root
value = 64
print("Square root of", value, ":", math.sqrt(value))
# Datetime: display current date and time
current = datetime.now()
print("Current date and time:", current)'''
'''#Expense Tracker
from datetime import datetime
expenses = []
def add_expense():
    try:
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        expense = {
            "item": item,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        expenses.append(expense)
        with open("expenses.txt", "a") as file:
            file.write(f"{expense['date']} - "
                       f"{expense['item']} - "
                       f"{expense['amount']}\n")
        print("Expense added successfully.")
    except ValueError:
        print("Error: Please enter a valid amount.")
def view_expenses():
    if not expenses:
        print("No expenses available.")
        return
    for expense in expenses:
        print(expense)
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")'''
"""#Classes and Objects 
class Student:
    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
student1 = Student()
student1.name = "Venkatesh"
student1.course = "CSE-DS"
student1.marks = 85
student2 = Student()
student2.name = "Priya"
student2.course = "CSE"
student2.marks = 90
student1.display()
print()
student2.display()"""
"""#Constructors
class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
student1 = Student("venkatesh", "CSE-DS", 85)
student2 = Student("My love", "CSE", 90)
student1.display()
print()
student2.display()"""
"""# Inheritance
class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
    def show_course(self):
        print("Course:", self.course)
student = Student("Venkateswara Reddy", "CSE-DS")
student.show_name()
student.show_course()"""
"""# Polymorphism
class Dog:
    def sound(self):
        print("Dog says: Woof!")
class Cat:
    def sound(self):
        print("Cat says: Meow!")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()"""
"""# Encapsulation & Abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UpiPayment(Payment):
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    def get_balance(self):
        return self.__balance
    def pay(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Payment successful:", amount)
        else:
            print("Payment failed: check amount or balance")
payment = UpiPayment(1000)
print("Balance before:", payment.get_balance())
payment.pay(250)
print("Balance after:", payment.get_balance())
payment.pay(2000)"""
"""#9palindrome
class palindrome:
     def nums(self,number):
         self number = '121'
     def display(self):
     print(self,number) """
"""#sum of the digits and product
class digits:
    def product_and_sum(self,n):
        s = 0
        p = 1
        while n > 0:
            d=n%10
            s +=d
            p*=d
            n//=10
d=digits()
n=int(input())
d.product_and_sum(n)"""
"""#odd num1523
class digits:
    def  pro_and_sum(self,low,high):
        c=0
        for i in range(low,high+1):
            if i%2!=0:
                c+=1
        print(c)
d=digits()
high=int(input())
low=int(input())
d.pro_and_sum(high,low)
"""
#258 add digits
class digits:
    def addDigits(self, num):
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num
s = digits()
print(s.addDigits(48))
print(s.addDigits(0))

     
     






























































    






         


      
