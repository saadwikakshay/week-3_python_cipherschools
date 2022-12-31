'''Generators'''
def Generate_squares(n):
    print([ i**2 for i in range (1,n)])
n=int(input("n: "))
Generate_squares(n)

#Lazy loading
def generate_squares(n):
    for i in range(1, n):
        yield i**2
n=int(input())
Generate_squares(n)

def func():
    print("start")
    yield 1 
    print("yielded 1")
    yield 2 
    print("yielded 2")
func()
it = iter(func())
print(it)

def func():
    print("started")
    yield
    sleep(5)
    print("ended")
func()
print("hello")
it = iter(func())
next(it)
print("world")
next(it)

a=( i**2 for i in range(10))
print(type(a))

a=Generate_squares(16):
print(next(a))