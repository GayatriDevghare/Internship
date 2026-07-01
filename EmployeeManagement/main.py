from Employee_management import EmployeeManagement

ems = EmployeeManagement()

while True:

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        ems.add_employee()

    elif choice == "2":
        ems.view_employees()

    elif choice == "3":
        ems.search_employee()

    elif choice == "4":
        ems.update_employee()

    elif choice == "5":
        ems.delete_employee()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")