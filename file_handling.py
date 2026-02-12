'''
open
read/write
close

'''

'''s=open('demo.txt.py',mode='r')
print(s.read())
s.close()'''

'''s=open('demo.txt.py',mode='w')
s.write('hello world')
s.close()'''

'''s=open('demo.txt.py',mode='a')
s.write('bye bye hellowrite')
s.close()'''

'''s=open('demo.txt.py',mode='r+')
print(s.read())
s.write('r+mode')
s.close()'''

'''s=open('demo.txt.py',mode='w+')
s.write('w+ mode')
s.seek(0)
print(s.read())
s.close()'''

s=open('demo.txt.py',mode='w+')

s.write('heluuuuuuuulo world')
s.seek(0)
print(s.read())
s.close()

