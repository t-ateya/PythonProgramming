"""
    instantiating a class

    When we call a class, a class instance object is created.
    This class instance object has its own namepace distinct from that of the class used to create the object

    This object has some attributes Python automatically implements for us:
        -> __dict__ is the object local namespace
        -> __class__ tells us which class was used to instantiate the object
            -> prefer using type(obj) istead of obj.__class__

"""
class MyClass:
    pass 

m = MyClass()

print(type(m))
print(m.__class__)