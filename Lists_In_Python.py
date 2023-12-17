list = ["Name", 1] ## Different Data Types A re Allowed
## But not in Tuple
print(list)
print(list[0])
print(list[1])
## Same Thing Applies For Strings Too
if "Name" in list : 
    print("Name is Present")
else : 
    print("Number Is Not Present")

list.append(4) ## To append one value
print(list)
Number = [7,4,5,4,2,0,1,123,859,1561,36456,315,1560,1616]
Number.reverse()
print(Number) ## Reverse The List
Number.sort() ## Sorting A List in ascending order
print(Number)
Number.sort(reverse=True) ## Sorting A List in Descending order
print(Number)
print(Number.index(1)) ## Give The First Occurence of Given Number 1
print(Number.count(76)) ## Give The Total Count Of 76

m = Number.copy() ## Creates A Copy Of Number
m = Number ## Acts as a Reference To Number
## NOT RECOMMENDED
Number.insert(12,45789765) ## Enter The Number At 12th Index
print(Number)

n = ["This is an example of using Extend in Lists"]
Number.extend(n) ## Add n in the end Of Number List
print(Number) 
k = Number + m + n ## Concatinating Two or More Lists w/o changing the individual Lists
print(k)