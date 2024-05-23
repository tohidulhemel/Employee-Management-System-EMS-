import os

class Employee:
    def __init__(self, emp_id, name, age, position):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f'{self.emp_id},{self.name},{self.age},{self.position}'

def add_employee(emp):
    with open('employees.txt', 'a') as file:
        file.write(str(emp) + '\n')

def view_employees():
    if not os.path.exists('employees.txt'):
        print("No employees found.")
        return
    with open('employees.txt', 'r') as file:
        employees = file.readlines()
        for emp in employees:
            print(emp.strip())

def search_employee(emp_id):
    if not os.path.exists('employees.txt'):
        print("No employees found.")
        return
    with open('employees.txt', 'r') as file:
        employees = file.readlines()
        for emp in employees:
            emp_details = emp.strip().split(',')
            if emp_details[0] == emp_id:
                print(emp.strip())
                return emp_details
        print("Employee not found.")
        return None

def delete_employee(emp_id):
    if not os.path.exists('employees.txt'):
        print("No employees found.")
        return
    with open('employees.txt', 'r') as file:
        employees = file.readlines()
    with open('employees.txt', 'w') as file:
        found = False
        for emp in employees:
            emp_details = emp.strip().split(',')
            if emp_details[0] != emp_id:
                file.write(emp)
            else:
                found = True
        if found:
            print(f"Employee {emp_id} deleted.")
        else:
            print("Employee not found.")

def update_employee(emp_id):
    if not os.path.exists('employees.txt'):
        print("No employees found.")
        return
    with open('employees.txt', 'r') as file:
        employees = file.readlines()

    new_employees = []
    found = False
    for emp in employees:
        emp_details = emp.strip().split(',')
        if emp_details[0] == emp_id:
            found = True
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            position = input("Enter new position: ")
            updated_emp = Employee(emp_id, name, age, position)
            new_employees.append(str(updated_emp) + '\n')
        else:
            new_employees.append(emp)

    if found:
        with open('employees.txt', 'w') as file:
            file.writelines(new_employees)
        print(f"Employee {emp_id} updated.")
    else:
        print("Employee not found.")

def main():
    while True:
        print("{:>60}".format("************************************"))
        print("{:>60}".format("-->> Employee Management System <<--"))
        print("{:>60}".format("************************************"))
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Update Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            position = input("Enter Position: ")
            emp = Employee(emp_id, name, age, position)
            add_employee(emp)
        elif choice == '2':
            view_employees()
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            search_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(emp_id)
        elif choice == '5':
            emp_id = input("Enter Employee ID to update: ")
            update_employee(emp_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
