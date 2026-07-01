from employee_management import EmployeeService
s=EmployeeService()
while True:
    print("\n============Employee Management System==============")
    print("\n1.Add Employee :\n2.View Employee :\n3.Search Employee :\n4.Update Employee :\n5.Delete Employee :\n6.Exit :")
    ch=input("Choice: ")
    if ch=="1": s.add_employee()
    elif ch=="2": s.view_employees()
    elif ch=="3": s.search_employee()
    elif ch=="4": s.update_employee()
    elif ch=="5": s.delete_employee()
    elif ch=="6": break
    else: print("Invalid Choice")
