#1. Input & Output
#Take your name and age as input and print them.
'''name=input("enter your name:")
age=int(input("enter your age:"))
print(name)
print(age)
#Take two numbers as input and print their sum.
x=int(input("enter x value:"))
y=int(input("enter y value:"))
sum=x+y
print(sum)
#Take your name as input and print: Hello, Deeksha!
name=input("enter your name:")
print("Hello, " + name + "!")
print(f"Hello, {name}!")'''


#2. String Manipulation
#Take a name as input and print its length.
'''name=input("enter your name:")
print(len(name))
#Take two strings and join them together.
start_name="deeksha"
last_name="gowda"
full_name=start_name+last_name
print(full_name)
#Repeat a string multiple times using the * operator.
name="abhi " * 3
print(name)'''


#3. String Methods
#Take a string and use upper(), lower(), and title().
'''message="Hello EveryOne!!"
print(message.upper())
print(message.lower())
print(message.title())
#Take a string containing extra spaces and remove them using strip().
message= "   good morining my dear!   "
print(message.strip())
#Take a sentence and replace one word with another using replace().
message="Hello Sir!!"
print(message.replace("Sir","Mam"))


#4. Accessing String Characters
#Take a word and print its first and last character.
word="Java"
print(word[0])
print(word[3])
#Take a word and print the character at index 2.
word="python"
print(word[2])


#5. Slicing Strings
#Take a string and print its first 3 characters.
text="Meet you today"
print(text[0:3])
#Take a string and print its last 3 characters.
text="Meet you today"
print(text[-3:])'''


#6. Comments & Escape Sequences
#Write a Python program containing both a single-line comment and a multi-line comment.
#this is single line comment
print("Hello, world!")
'''multi line comment
of this sentence'''
print("Hello, world!")
#Print the following using escape sequences:
#Hello
#Python
#"Learning is fun!"
print("Hello\npython\n\"learning is fun!\"")
