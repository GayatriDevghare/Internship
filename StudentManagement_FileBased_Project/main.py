from student_management import StudentService
s=StudentService()
while True:
    print("\n============Student Management System==============")
    print("\n1.Add Student :\n2.View Student :\n3.Search Student :\n4.Update Student :\n5.Delete Student :\n6.Exit :")
    ch=input("Choice: ")
    if ch=="1": s.add_student()
    elif ch=="2": s.view_students()
    elif ch=="3": s.search_student()
    elif ch=="4": s.update_student()
    elif ch=="5": s.delete_student()
    elif ch=="6": break
    else: print("Invalid Choice")
