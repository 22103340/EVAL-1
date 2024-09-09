employees = {};
def add_employee(emp_id, name, department, salary):
    employees[emp_id] = {'name': name, 'department': department, 'salary': salary}
def update_employee(emp_id, name=None, department=None, salary=None):
    if emp_id in employees:
        if name is not None:
            employees[emp_id]['name'] = name
        if department is not None:
            employees[emp_id]['department'] = department
        if salary is not None:
            employees[emp_id]['salary'] = salary
    else:
        print("Employee ID not found.")
def search_employee(emp_id):
    return employees.get(emp_id, "Employee ID not found.")
def department_report():
    report = {}
    for emp in employees.values():
        dept = emp['department']
        if dept not in report:
            report[dept] = []
        report[dept].append(emp)
    return report
def print_department_report():
    report = department_report()
    for dept, emps in report.items():
        print(f"Department: {dept}")
        for emp in emps:
            print(f"  ID: {emp['id']}, Name: {emp['name']}, Salary: {emp['salary']}")
        print()
def main():
    add_employee(1, 'GARV', 'MATHS', 10000000)
    add_employee(2, 'HEMANT', 'PHYSICS', 4200000)
    add_employee(3, 'ANANT', 'COMPUTER SCIENCE', 3500000)
    
    print(search_employee(1))
    update_employee(1, salary=5200000)
    print (search_employee(1))
    print (department_report())
main()
    
    
