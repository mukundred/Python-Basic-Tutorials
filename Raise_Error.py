a= int(input("Enter a Number Between 0-100 : "))
if(a>100 or a<0) :
    raise ValueError("Value Should be between 0-100") ## Raise an Error
