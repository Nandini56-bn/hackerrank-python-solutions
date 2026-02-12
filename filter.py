#filter(function-name,sequence-variable)
#print even numbers 1 to 10
'''l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list(filter(lambda n:n%2==0,range(1,11))))'''


#reduce () function
# from function import reduce
#reduce(function-name,sequence-variable)
#sum of first 10 natural numbers
'''l=[1,2,3,4,5,6,7,8,9,10,1]
result=reduce(lambda x,y:x+y,l)
print(result)'''


from functools import reduce
l=[1,2,3,4,5,6]
result=reduce(lambda x,y:x+y,l)
print(result)

