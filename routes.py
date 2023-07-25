from run import app,db
from flask import jsonify
from models import Employee,EmployeeSchema
from flask import request
try:            
    employee_schema= EmployeeSchema()            
    kwargs = {"strict": True}       
except TypeError:         
    kwargs = {}

try:            
    employees_schema= EmployeeSchema(many=True)            
    kwargs = {"strict": True}       
except TypeError:         
    kwargs = {}

@app.route('/employee',methods=["POST"])
def add_employee():
    name=request.json["name"]
    age=request.json["age"]
    designation=request.json["designation"]
    salary=request.json["salary"]

    new_employee=Employee(name,age,designation,salary)
    db.session.add(new_employee)
    db.session.commit()
    return employee_schema.jsonify(new_employee)

@app.route('/employee',methods=['GET'])
def get_employees():
    emp=Employee.query.all()
    result=employees_schema.dump(emp)
    return jsonify(result)

@app.route('/employee/<id>',methods=['GET'])
def get_employee(id):
    emp=Employee.query.get(id)
    return employee_schema.jsonify(emp)

@app.route('/employee/<id>',methods=['PUT'])
def update_employee(id):
    emp=Employee.query.get(id)
    name=request.json["name"]
    age=request.json["age"]
    designation=request.json["designation"]
    salary=request.json["salary"]

    emp.name=name
    emp.age=age
    emp.designation=designation
    emp.salary=salary
    db.session.commit()
    return employee_schema.jsonify(emp)


@app.route('/employee/<id>',methods=['DELETE'])
def delete_employee(id):
    emp=Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return employee_schema.jsonify(emp)



