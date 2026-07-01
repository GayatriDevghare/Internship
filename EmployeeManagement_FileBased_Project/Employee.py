class employee:
    def __init__(self,id,name,age):
        self.id=id 
        self.name=name 
        self.age=age
    def __str__(self):
        return f"{self.id},{self.name},{self.age}"
