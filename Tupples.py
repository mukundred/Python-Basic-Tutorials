## This is the Programme to tell you about the Tuples
tup = (31567, "hdsahoc",67382.732819, "Random") ## Creating a tuple with spherical brackets
# tuple[0] = 65478 This Line Will Throw Error as Tuples are non changeable
print(tuple)
t1 = (1)
print(type(t1)) ## will show int as you have to add , after every addition in the tuple
t1 = (1, )
print(type(t1)) ## will print tuple as the types
print(tuple[:4]) ## Slicing in a Tupple

temp = list(tup)
temp.append("Applying operations in tupple by Converting it to a list")
temp[0] = "Adding a different Number"
tup = tuple(temp)
print(tup)