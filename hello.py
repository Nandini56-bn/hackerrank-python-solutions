#map,filter,reduce functions are there
#map(function.name,sequence-variable)
def square(n):
    return n*n


l=[1,2,3,4,5]
print(list(map(square,range(1,6))))
