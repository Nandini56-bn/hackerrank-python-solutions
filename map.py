'''def square(n):
    return n*n


l=[1,2,3,4,5]
print(list(map(square,range(1,6)))) '''



#using lambda in map function
#l=[1,2,3,4,5]
#print(list(map(lambda n:n*n,range(1,6))))

#using tuple
'''nums=[1,2,3]
res=tuple(map(lambda x:x+5,nums))
print(res)''' #(6,7,8)
#using set()
nums=[1,2,3,4,5]
res=set(map(lambda x:x*5,nums))
print(res)
#o/p:{5,10,15,20,25}



