from Employee import employee
class EmployeeService:
    FILE="employee.txt"
    def add_employee(self):
        id=input("Enter ID: ")
        try:
            open(self.FILE)
        except FileNotFoundError:
            open(self.FILE,"w").close()
        with open(self.FILE) as f:
            for line in f:
                if line.split(",")[0]==id:
                    print("ID already exists"); return
        name=input("Enter Name: "); age=input("Enter Age: ")
        with open(self.FILE,"a") as f:
            f.write(str(employee(id,name,age))+"\n")
        print("Employee Added Successfully!")
        print("-------------------------------------------------------------------")
        
        
    def view_employees(self):
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
        
        
    def search_employee(self):
        id=input("Enter ID: ")
        try:
            with open(self.FILE) as f:
                for r in f:
                    i,n,a=r.strip().split(",")
                    if i==id:
                        print("Found:",i, n ,a); 
                        return
            print("Employee Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
        
        
    def update_employee(self):
        id=input("Enter ID: ")
        try:
            with open(self.FILE) as f: rows=f.readlines()
            found=False
            with open(self.FILE,"w") as f:
                for r in rows:
                    i,n,a=r.strip().split(",")
                    if i==id:
                        n=input("New Name: "); a=input("New Age: "); found=True
                    f.write(f"{i},{n},{a}\n")
            print("Employee Updated Successfully" if found else "Employee Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
        
        
    def delete_employee(self):
        id=input("Enter ID: ")
        try:
            with open(self.FILE) as f: rows=f.readlines()
            found=False
            with open(self.FILE,"w") as f:
                for r in rows:
                    if r.split(",")[0]!=id: f.write(r)
                    else: found=True
            print("Employee Deleted Successfully" if found else "Employee Not Found")
        except FileNotFoundError:
            print("No Records")
        print("-------------------------------------------------------------------")
