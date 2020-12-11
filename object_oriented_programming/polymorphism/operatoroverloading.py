class Books:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self,other):
        return self.pages+other.pages

obj=Books(100)
obj1=Books(200)
print(obj+obj1)
print(type(obj))
