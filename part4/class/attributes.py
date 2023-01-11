class MyClass:
    language = 'Python'
    version = '3.6'

"""
    getattr function              getattr(object_symbol, attribute_name, optional_default)

    getattr(MyClass, 'language')               ->   'Python'

    getattr(MyClass, 'x')             -> AttributeError exception

    getattr(MyClass, 'x', 'N/A')              ->'N/A'

    MyClass.language                -> 'Python'

    Setting Attribute Values in Objects

    setattr(MyClass, 'version', '3.7')

    delattr(MyClass, 'version') or del MyClass.version

    The following are similar:
        - MyClass.language
        - getattr(MyClass, 'language')
        - MyClass.__dict__['language']  #not a good practice. Does not always work

"""

class Program:
    language = "Python"
    version = "3.7"

setattr(Program, 'x', -100)

Program.y = "ehllo"
print(Program.__dict__)
print(Program.__name__)

del Program.y

print(Program.__dict__)
