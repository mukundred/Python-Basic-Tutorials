a = "\"Your Name , Please Tell\", said Master Yoda"
print(a[3]) ## Output : u
## String Length
length = len(a)
print(a[0:length]) ## The Whole String
print("The Length Of The String is", length)
print("The Speaker Of These Lines is", a[32:length])

b = a[32:length] ## Storing The Name in another place

print("The Length Of Name is", len(b))
print(b[-4:-2])
## This Above Line Means 11-4 to 11-2, i.e 7-9
## So Word from 7->9 will be printed
print(b.upper()) ## print string in UPPER CASES
print(b.lower()) ## PRINT STRING IN lower cases

### Some More Examples
# Strings are immutable
a = "!!! Corleone!! !!!!!!!!! Godfather"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
