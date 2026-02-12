#multiple inheritance
'''class student():
    def studyl(self):
        print("i am a student")
class teacher(student):
    def studys(self):
        print("i am a teacher")
class hod(teacher,student):
    def study(self):
        print("i am a hod")

obj=hod()
obj.study()
obj.studys()
obj.studyl()'''


#hierarchical inheritance
'''class student():
    def show(self):
        print("i am a student")
class teacher(student):
    def shows(self):
        print("i am a teacher")
class teacher2(student):
    def showl(self):
        print("i am a teacher2")
obj=teacher()
obj2=teacher2()
obj.shows()
obj.show()
obj2.showl()
obj2.show()'''

#multilevel inheritance
'''class student():
    def studyl(self):
        print("i am a student")
class teacher(student):
    def studys(self):
        print("i am a teacher")
class hod(teacher):
    def study(self):
        print("i am a hod")

obj=hod()
obj.study()
obj.studys()
obj.studyl()'''

#single inheritance
'''class student():
    def study(self):
        print("i am a student")
class teacher(student):
    def studys(self):
        print("i am a teacher")
obj=teacher()
obj.studys()
obj.study()'''

'''class student():
    def study(self):
        print("i am a student")
class teacher(student):
    def studys(self):
        print("i am a teacher")
t=teacher()
t.studys()
t.study()'''

'''class hod():
    def studysg(self):
        print("i am a hod")
class teacher():
    def study(self):
        print("i am a student")
class student(hod,teacher):
    def studys(self):
        print("i am a teacher")
t=student()
t.studys()
t.study()
t.studysg()'''

class hod():
    def study(self):
        print("i am a hod")
class student1(hod):
    def studys(self):
        print("i am a student1")
class student2(hod):
    def studysf(self):
        print("i am a student2")
s=student1()
s1=student2()
s.studys()
s.study()
s1.studysf()
s1.study()





