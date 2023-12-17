def func1() : 
    ## It will be considered a doc string if and only if it's written write after function
    '''
    A Function to Greet Humans 
    '''
    print("Hello Sir, How do you do ?")

func1()
print(func1.__doc__) ## print the string about the defintion of functions, classes and objects
 
