import routes
from run import db,m


class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    designation=db.Column(db.String(40),nullable=False)
    salary=db.Column(db.Integer,nullable=False)

    def __init__(self,name,age,designation,salary):
        self.name=name
        self.age=age
        self.designation=designation
        self.salary=salary

class  EmployeeSchema(m.Schema):
    class Meta:
        fields=('id','name','age','designation','salary')





    
