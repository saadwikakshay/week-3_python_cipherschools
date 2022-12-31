class SchoolMember:
    '''Represents any school members.'''
    def __init__(self, name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMembers: {})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age, salary)
        self.salary = salary
        print('(Initialized Teacher: "{}")'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class A:
    def __init__(self, n):
        print("A init executed")
class B(A):
    def __init__(self):
        super()
        print("B init executed")



#MRO (Method Resolition Order)

class A:
    pass
class B(A):
    print("x=5")
class C(B):
    pass
class D(A):
    print("x=10")
class E(C, D):
    pass

c=E()
#print(e.x)

#E.mro()
#[__main__.E,__main__.C,__main__.B,__main.D,__main.A, object]

#iteratin Protocol
#for ant object to be an iterable ,it should have 2 dunders
#__iter__
#__next__

a=range(5)
it=a.__iter__()

class myrange:
    def __init__(self,n):
        self.n 
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0
    def __next__(self):
        ret = self.i
        self.i += 10
        if ret >= self.myrange.n:
            raise Stopiteration
        return ret

a=[1,2,3,4]
print(iter(a))