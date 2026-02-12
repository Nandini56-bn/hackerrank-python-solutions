#comprehension means combining for loop +if condition as one


#list comprehension
#l=[expr for var in sequence]
#l=[i**3 for i in range(1,11)]
#rint(l)
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''l=[] #using for loop
for i in range(1,11):
    l.append(i**3)
print(l)'''
'''#l=[expression for variable in sequence]

print([i**3 for i in range(1,11)])'''
# if condition use chestu
'''l=[i for i in range(0,11) if i%2==0]
print(l)
[0, 2, 4, 6, 8, 10]'''


#dict comprehension
#same syntax but in place of [] this in dict we use {} this
'''d={i:i*1 for i in range(1,6)}
print(d)'''
#o/p:{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}



#set comprehension
'''s={i*i for i in range (1,6)}
print(s)'''
#{1, 4, 9, 16, 25}
