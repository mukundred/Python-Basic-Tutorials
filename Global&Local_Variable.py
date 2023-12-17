x = 5 ## Global Variables
print(f"The value of x outside function is {x}")
def hello():
    # x = 8 ## Local Variables
    # print(f"The value of x inside function is {x}")
    print("Hello Sir")
    global x ## Change X value
    x= 9
    print(x)

hello()
print(x)