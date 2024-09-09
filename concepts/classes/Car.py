class Car1:
    
    def __new__(cls):
        print('<< new >>')
        
    def __init__(self):
        print('<< init >>')

#Note: __init__ is a method to init instance variable (it is a kind of constructor for programming languages like Java)
#__new__ is used to customize actions when we are creating instances.
#__new__ and __init__ allow to access to differents moments in the process of object creation.

car = Car1()
print('---------------------------------')

#output: << new >>, because __new__ isn't returning the instance, and __init__ is not called.


class Car2:
    
    def __new__(cls):
        print('<< new >>')
        return super(Car2, cls).__new__(cls)
        
    def __init__(self):
        print('<< init >>')

car = Car2()
print('---------------------------------')

#output: << new >> and << init >> because __new__ is returning the instance


class Car3:
    
    def __new__(cls):
        print('<< new >>')
        return super(Car3, cls).__new__(cls)
        
    def __init__(self):
        print('<< init >>')
        
    def __del__(self):
        print('<< del >>')

car = Car3()
#__del__ is a destructor method to remove an instance, it's an analogy of the Java's Garbage collector
# This method could be called to create instructions in the specific moment that the instance will destroy.


