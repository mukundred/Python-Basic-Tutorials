# MAPS
def cube(x) :
    return x*x*x
l = [1,2,3,4,5,6,7,8,9,9,0,9,7,6,5,4,4,3,2,2]
newl = list(map(cube , l))
 
print(newl)

#FILTERS
def filter_functions(a) : 
    return a>4

nl = list(filter(filter_functions, l))
print(nl)

#Reduce
from functools import reduce
number = [78974,465,4561,123,489,156,753]
def sum(x,y) : 
    return x+y

sum = (reduce(sum,number))
print(sum)