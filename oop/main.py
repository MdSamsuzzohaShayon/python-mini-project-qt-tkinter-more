# SCOPE
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

print("----------------")


# CLASS
# Class objects support two kinds of operations: attribute references and instantiation.
class Simple:
    # creates a new instance of the class and assigns this object to the local variable x
    # a class may define a special method named __init__()
    def __init__(self):
        print("this is constructor")
        self.data = "This is data from constructor"

    """A simple example class"""

    i = 12345

    def f(self):
        print(self.data)
        return 'hello world'


x = Simple()
print(x.f())


# AFTER SIMPLE

# the __init__() method may have arguments for greater flexibility
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


cplx = Complex(3.0, -4.5)
print("Passing parameters to constructor: ", cplx.r, cplx.i)

# Instance Objects
# There are two kinds of valid attribute names: data attributes and methods.
cplx.counter = 1
while cplx.counter < 10:
    cplx.counter = cplx.counter * 2
print("Complex counter: ", cplx.counter)
del cplx.counter


# Method Objects
# https://docs.python.org/3/tutorial/classes.html#method-objects
# cplx.f()
# xf = cplx.f
# while True:
#     print("Method object: ",xf())


# Class and Instance Variables¶
# instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:
class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)



print("---------")

# Random Remarks
# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)





# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)






