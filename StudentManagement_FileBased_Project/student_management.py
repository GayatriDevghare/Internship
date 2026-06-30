from student import Student
class StudentService:
    FILE="students.txt"
    def add_student(self):
        sid=input("Enter ID: ")
        try:
            open(self.FILE)
        except FileNotFoundError:
            open(self.FILE,"w").close()
        with open(self.FILE) as f:
            for line in f:
                if line.split(",")[0]==sid:
                    print("ID already exists"); return
        name=input("Enter Name: "); age=input("Enter Age: ")
        with open(self.FILE,"a") as f:
            f.write(str(Student(sid,name,age))+"\n")
        print("Student Added Successfully!")
        print("-------------------------------------------------------------------")
        
        
    def view_students(self):
        try:
            with open(self.FILE) as f:
                rows=f.readlines()
            if not rows: print("No Records"); return
            print("ID,\tName,\tAge")
            for r in rows:
                i,n,a=r.strip().split(","); print(f"{i}\t{n}\t{a}")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
        
        
    def search_student(self):
        sid=input("Enter ID: ")
        try:
            with open(self.FILE) as f:
                for r in f:
                    i,n,a=r.strip().split(",")
                    if i==sid:
                        print("Found:",i, n ,a); 
                        return
            print("Student Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
        
        
    def update_student(self):
        sid=input("Enter ID: ")
        try:
            with open(self.FILE) as f: rows=f.readlines()
            found=False
            with open(self.FILE,"w") as f:
                for r in rows:
                    i,n,a=r.strip().split(",")
                    if i==sid:
                        n=input("New Name: "); a=input("New Age: "); found=True
                    f.write(f"{i},{n},{a}\n")
            print("Student Updated Successfully" if found else "Student Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
        
        
    def delete_student(self):
        sid=input("Enter ID: ")
        try:
            with open(self.FILE) as f: rows=f.readlines()
            found=False
            with open(self.FILE,"w") as f:
                for r in rows:
                    if r.split(",")[0]!=sid: f.write(r)
                    else: found=True
            print("Student Deleted Successfully" if found else "Student Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
