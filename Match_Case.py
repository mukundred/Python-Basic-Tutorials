x = int(input("Enter Your Age : "))
match x:
    case 0:
        print("Call Your Parents !!!")
    case 18:
        print("You are 18, That's Great")
    case _ if 10 < x <= 17:
        print("Go To School & Study")
        print("Your Age is", x)
    case _:
        print("Your Age is", x)
