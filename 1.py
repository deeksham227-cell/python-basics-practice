#1. Variables in Python
#Create a variable name and store your name in it. Print it.
name="Deeksha"
print(name)
#Create variables for your name, age, and college and print all three.
name="anu"
age=20
college="xyz"
print(name)
print(age)
print(college)


#2. Data Types in Python
#Take your age as input and print its data type.
age=int(input("enter age:"))
print(type(age))
#Create variables containing an integer, float, string, and boolean. Print their values and data types.
marks=20
per=95.5
sub="science"
passed=True
print(marks,type(marks))
print(per,type(per))
print(sub,type(sub))
print(passed,type(passed))


#3. Type Conversion
#Convert 25 into a float and print it.
marks=25
marks_as=float(marks)
print(marks_as)
#Convert "50" into an integer and add 10.
total="50"
total_as=int(total)
total_as+=10
print(total_as)
#Take two numbers as input and add them after converting them to integers.
x=int(input("enter x value:"))
y=int(input("enter y value:"))
print(x+y)


#4. Arithmetic Operators
#Write a program to add two numbers.
a=20
b=5
c=a+b
print(c)
#Write a program to subtract two numbers
a=20
b=5
c=a-b
print(c)
#Write a program to multiply two numbers.
a=20
b=5
c=a*b
print(c)
#Write a program to divide two numbers.
a=12
b=5
c=a/b
print(c)
#Find the remainder when 25 is divided by 4.
a=25
b=4
c=a%b
print(c)
#Find the quotient using floor division: 25 // 4.
a=25
b=4
c=a//b
print(c)
#Find 5 raised to the power 3.
a=5
b=3
c=a**b
print(c)
#Take two numbers from the user and perform + , - , * , / on them.
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
#Find the square and cube of a number.
num=int(input("enter the number:"))
square=num**2
cube=num**3
print("square=",square)
print("cube=",cube)


#Assigning Values to Multiple Variables
#Assign 10, 20, and 30 to three variables in one line and print them.
x,y,z=5,10,20
print(x)
print(y)
print(z)
#Assign the same value 100 to three variables in one statement.
x=y=z=100
print(x)
print(y)
print(z)
#Assign your name, age, and city to three variables in one line.
name,age,city="asha",15,"bangalore"
print(name)
print(age)
print(city)
#Create a, b, c and assign 5, 10, 15 respectively. Find their sum.
a=5
b=10
c=15
sum=a+b+c
print(sum)


#Variable Reassignment
#Create x = 10. Change its value to 20 and print it.
x=10
x=20
print(x)
#Create name = "Deeksha". Reassign it to another name and print the new value.
name="Deeksha"
name="anu"
print(name)
#create marks = 50. Increase it to 75 using reassignment
marks=50
marks=75
print(marks)
#Create x = 10, then multiply its value by 2 using reassignment.
x=10
x=x*2
print(x)
#Create price = 500, reduce it by 100 using reassignment.
price=500
price=price-100
print(price)


#Create two variables, swap their values using a third variable.
a=20
b=10
temp=a
a=b
b=temp
print("a=",a)                                     
print("b=",b)
#Swap two variables without using a third variable.
a=10
b=5
a,b=b,a
print(a)
print(b)






