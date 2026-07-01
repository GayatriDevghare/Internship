from Employee import Employee
from db import conn, cursor

class EmployeeManagement:

    # Add Employee
    def add_employee(self):

        try:
            id = int(input("Enter Employee ID : "))
            name = input("Enter Employee Name : ")
            age = int(input("Enter Employee Age : "))

            employee = Employee(id, name, age)

            sql = "INSERT INTO employee VALUES (%s,%s,%s)"
            values = (employee.id, employee.name, employee.age)

            cursor.execute(sql, values)
            conn.commit()

            print("Employee Added Successfully")

        except Exception as e:
            print("Error :", e)

    # View Employees
    def view_employees(self):

        cursor.execute("SELECT * FROM employee")

        employees = cursor.fetchall()

        if len(employees) == 0:
            print("No Records Found")
            return

        print("\n-----------------------------")
        print("ID\tNAME\tAGE")
        print("-----------------------------")

        for e in employees:
            print(e[0], "\t", e[1], "\t", e[2])

    # Search Employee
    def search_employee(self):

        id = int(input("Enter Employee ID : "))

        cursor.execute("SELECT * FROM employee WHERE id=%s", (id,))

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found")
            print("ID :", employee[0])
            print("Name :", employee[1])
            print("Age :", employee[2])
        else:
            print("Employee Not Found")

    # Update Employee
    def update_employee(self):

        id = int(input("Enter Employee ID : "))

        name = input("Enter New Name : ")
        age = int(input("Enter New Age : "))

        cursor.execute(
            "UPDATE employee SET name=%s, age=%s WHERE id=%s",
            (name, age, id)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Employee Updated Successfully")
        else:
            print("Employee Not Found")

    # Delete Employee
    def delete_employee(self):

        id = int(input("Enter Employee ID : "))

        cursor.execute(
            "DELETE FROM employee WHERE id=%s",
            (id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Employee Deleted Successfully")
        else:
            print("Employee Not Found")