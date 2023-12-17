dic = {"Person" : "Human Being", "NULL":"Zero", "Something" : "Someone"}
print(dic["NULL"]) ## Output Zero
# print(dic["Something Which is Not There?"]) ## Will Throw Error
print(dic.get("Something Which is Not There ?")) ## Willl Not Throw Error
print(dic)
print(dic.keys()) ## Print Keys
print(dic.values()) ## Print Values
# for key in dic.keys() : 
#     print(dic[key])

for key in dic.keys() : 
    print(f"The value Corresponding to the key {key} is {dic[key]}")