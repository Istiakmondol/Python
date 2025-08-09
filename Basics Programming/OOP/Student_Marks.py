class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"Hello {self.name} Your average marks is {sum/len(self.marks):.2f}")
        
student=Student("Istiak",[87,49,91])
student.avg()

    

