from student import Student
from db import conn, cursor

class StudentManagement:

    # Add Student
    def add_student(self):

        try:
            sid = int(input("Enter Student ID : "))
            name = input("Enter Student Name : ")
            age = int(input("Enter Student Age : "))

            student = Student(sid, name, age)

            sql = "INSERT INTO student VALUES (%s,%s,%s)"
            values = (student.sid, student.name, student.age)

            cursor.execute(sql, values)
            conn.commit()

            print("Student Added Successfully")

        except Exception as e:
            print("Error :", e)

    # View Students
    def view_students(self):

        cursor.execute("SELECT * FROM student")

        students = cursor.fetchall()

        if len(students) == 0:
            print("No Records Found")
            return

        print("\n-----------------------------")
        print("ID\tNAME\tAGE")
        print("-----------------------------")

        for s in students:
            print(s[0], "\t", s[1], "\t", s[2])

    # Search Student
    def search_student(self):

        sid = int(input("Enter Student ID : "))

        cursor.execute("SELECT * FROM student WHERE id=%s", (sid,))

        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print("ID :", student[0])
            print("Name :", student[1])
            print("Age :", student[2])
        else:
            print("Student Not Found")

    # Update Student
    def update_student(self):

        sid = int(input("Enter Student ID : "))

        name = input("Enter New Name : ")
        age = int(input("Enter New Age : "))

        cursor.execute(
            "UPDATE student SET name=%s, age=%s WHERE id=%s",
            (name, age, sid)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Updated Successfully")
        else:
            print("Student Not Found")

    # Delete Student
    def delete_student(self):

        sid = int(input("Enter Student ID : "))

        cursor.execute(
            "DELETE FROM student WHERE id=%s",
            (sid,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")