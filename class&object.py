class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def update_marks(self,newmarks):
        self.marks=newmarks

    def display(self):
        print(f"Grade : {self.marks}")

#creating 5 student objects
student1=student("valli",50)
student2=student("valli",60)
student3=student("valli",70)
student4=student("valli",80)
student5=student("valli",90)

student1.update_marks(90)
student2.update_marks(80)
student3.update_marks(70)
student4.update_marks(60)
student5.update_marks(50)

student1.display()
student2.display()
student3.display()
student4.display()
student5.display()
