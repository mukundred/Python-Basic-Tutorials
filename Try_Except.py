x = input("Enter A Number : ")
try : 
    for i in range (1,11) : 
        print(f"{int(x)} X {i} = {int(x)*i}") # Will Stop Running and go to Except
except Exception as e : 
    print("Some Error Occured")

print("Some Lines Of Code Which Were To Be Excepted to Run\n After Previous lines")
