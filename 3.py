                                                 #Operators 
#1. Assignment Operators
#Create x = 10, then use +=, -=, *=, and /= on it and print the result.
'''x=10
x+=15
print(x)
x-=5
print(x)
x*=2
print(x)
x/=8
print(x)'''
#Create marks = 50 and increase it by 10 using +=.
'''marks=50
marks+=10
print(marks)


#2. Comparison Operators
#Take two numbers and check whether they are equal.
a=20
b=30
print(a==b)
#Take two numbers and check which one is greater.
a=10
b=50
print( a>b )
print(b>a)
#Check whether a person's age is greater than or equal to 18.
age=25
print(age>=18)


#3. Logical Operators
#Take age and check whether the person is between 18 and 60 using and.
age=int(input("enter your age:"))
result=age>=18 and age<=60
print(result)
#Check whether a number is less than 10 or greater than 50 using or.
number=int(input("enter a number:"))
result=number<10 or number>50
print(result)
#Use not to reverse a boolean value.
a=20
print(not(a<50))


#4. Membership Operators
#Check whether "a" is present in the string "Python".
D="python"
print("a" in D)
#Check whether "apple" is present in a list of fruits.
my_list=["mango","cherry","apple"]
print("apple" in my_list)
#Check whether a particular name is not present in a list.
my_list=["anu","asha","disha"]
print("harsha" not in my_list)'''


#5. Bitwise Operators
#Perform AND (&) on 5 and 3.
a = 5
b = 3
print(a & b)
#Perform OR (|) on 5 and 3.
a = 5
b = 3
print(a | b)
#Perform XOR (^) on 5 and 3.
a = 5
b = 3
print(a ^ b)
#Perform left shift (<<) and right shift (>>) on a number.
a = 5
b = 3
print(a << 1)
print(a >> 1)