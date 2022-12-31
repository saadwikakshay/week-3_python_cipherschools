a=5
print(isinstance(a, object))

a=5
def func():
    pass
print(type(func))
func()
isinstance(func, object)

class A:
    name = "jatin"
    marks = 50
print(type(A))

class A:
    def __call__(self):
        print("You called me")
print(type(A))
a=A()

def func():
    print("Helo")
func()

a= {"name": "jatin"}
a["name"]
print(a.__getitem__("name"))

class Exponent:
    def __init__(self, x):
        self.n = n
    def __getitem__(self, x):
        return x ** self.n

class Dog:
    kind = "canino"
    def __init__(self, name):
        self.name = name

class Dog:
    tricks =[]
    def __init__(self, name):
        self.name = name
    def add_tricks(self, tricks):
        self.tricks.append(tricks)