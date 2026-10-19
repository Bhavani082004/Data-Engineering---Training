from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Employee Management API")

@app.get("/")
def root():
    return {
        "message": "Welcome to Employee Management API"
    }

class Employee(BaseModel):
    id: int
    name: str
    department: str
    designation: str
    salary: float
    city: str

employees: list[Employee] = []

@app.post("/employees", status_code=201)
def add_employee(employee: Employee):
    for emp in employees:
        if emp.id == employee.id:
            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )

    employees.append(employee)
    return employee

@app.get("/employees")
def get_all_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            if updated_employee.id != employee_id:
                raise HTTPException(
                    status_code=400,
                    detail="Employee ID cannot be changed"
                )

            employees[index] = updated_employee
            return updated_employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            employees.pop(index)

            return {
                "message": "Employee deleted successfully",
                "employee_id": employee_id
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
