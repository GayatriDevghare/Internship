class Student:
    def __init__(self,sid,name,age):
        self.sid=sid 
        self.name=name 
        self.age=age
    def __str__(self):
        return f"{self.sid},{self.name},{self.age}"
