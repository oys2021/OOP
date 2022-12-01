class Students:
    def __init__(self,age,name,grade):
        self.age=age
        self.name=name
        self.grade=grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade




class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.student=[]
    # def__init__(self,name,max_students):
    #     self.name=name
    #     self.max_students=max_students
    #     self.student=[]def__init__(self,name,max_students):
    #     self.name=name
    #     self.max_students=max_students
    #     self.student=[]
    
        
    def get_students(self,students):
        if len(self.student) < self.max_students:
            self.student.append(students)
            return True
        return False
        
    def get_average_grade(self):
        value=0
        for student in self.student:
            value +=student.get_grade()
        return value/len(self.student)
        
    
            
        
    def get_name(self):
        return self.name
    
    def get_max_students(self):
        return self.max_students

d=Students(45,"Kwaku",90)
d2=Students(45,"Bill",40)
d3=Students(15,"Kwaku",90)

c=Course("Physics",2)
c.get_students(d)
c.get_students(d2)
print(c.get_average_grade())

