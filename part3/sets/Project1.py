"""
    In this project, our goal is to validate one dictionary structure against a template dictionary.
    A typical example of this might be working with JSON data input in an API. You are trying to validate this received JSON against some kind of template to make 
    sure the received JSION conforms to that template (i.e all the keys and structure are idenitical - value types being important but not the value itself- so just hte structure
    , and the data type of the values).

    To keep things simple, we'll assume that values can be either single values (like an integer, string, etc), or a dictionary itself only containig single values
    or other dictinaries, recursively. In other words, we're not going to deal with lists as possible values. Also, to keep things simple, we'll assume that all
    keys are required, and that no extra keys are permitted.

    In practice, we would not have these simplifying assumptions, and although we could definitely write this ourselves, there are many third party libraries that
    already exist to do this (such as jsonschema, marshmallow, and many more, some of which will be covered in later videos)

    For example, you might have this template:
    
    template = {
        "user_id" : int, 
        "name" : {
            "first" : str,
            "last" : str
        },

        'bio' : {
            'dob': {
                'year': int,
                'month': int,
                'day': int
            },
            'birthplace':{
                'country': str,
                'city': str
            }
        }

    }

Example1. The data below will match the validation criteria

John = {
        "user_id" : 100, 
        "name" : {
            "first" : 'John',
            "last" : 'Cleese'
        },

        'bio' : {
            'dob': {
                'year': 1939,
                'month': 11,
                'day': 27
            },
            'birthplace':{
                'country': "United Kingdom",
                'city': "Weston-super-Mare"
            }
        }

    }

Ex2: This will not pass the template validation

Eric = {
        "user_id" : 100, 
        "name" : {
            "first" : 'Eric',
            "last" : 'Idle'
        },

        'bio' : {
            'dob': {
                'year': 1943,
                'month': 3,
                'day': 29
            },
            'birthplace':{
                'country': "United Kingdom"
            }
        }

    }


    michael = {
        "user_id" : 102, 
        "name" : {
            "first" : 'Michael',
            "last" : 'Palin'
        },

        'bio' : {
            'dob': {
                'year': 1943,
                'month': "May",
                'day': 5
            },
            'birthplace':{
                'country': "United Kingdom",
                'city': 'Sheffield'
            }
        }

    }


#Task
def validate(data, template):
    #implement
    #and return True/False
    #in the case of false, return a string describing 
    #the first error encountered
    #in the case of True, string can be empty
    return state, error

That should return this:
    . validate(John, template)-->True, ""
    . validate(eric, template)-->False, "mismatched keys: bio.birthplace.city"
    . validate(michael, template) --> False, "bad type: bio.dob.month"

"""

template = {
        "user_id" : int, 
        "name" : {
            "first" : str,
            "last" : str
        },

        'bio' : {
            'dob': {
                'year': int,
                'month': int,
                'day': int
            },
            'birthplace':{
                'country': str,
                'city': str
            }
        }

    }


John = {
        "user_id" : 100, 
        "name" : {
            "first" : 'John',
            "last" : 'Cleese'
        },

        'bio' : {
            'dob': {
                'year': 1939,
                'month': 11,
                'day': 27
            },
            'birthplace':{
                'country': "United Kingdom",
                'city': "Weston-super-Mare"
            }
        }

    }



Eric = {
        "user_id" : 100, 
        "name" : {
            "first" : 'Eric',
            "last" : 'Idle'
        },

        'bio' : {
            'dob': {
                'year': 1943,
                'month': 3,
                'day': 29
            },
            'birthplace':{
                'country': "United Kingdom"
            }
        }

    }


Michael = {
        "user_id" : 102, 
        "name" : {
            "first" : 'Michael',
            "last" : 'Palin'
        },

        'bio' : {
            'dob': {
                'year': 1943,
                'month': "May",
                'day': 5
            },
            'birthplace':{
                'country': "United Kingdom",
                'city': 'Sheffield'
            }
        }

    }

# Solution
class SchemaError(Exception):
    pass 
class SchemaKeyMismatch(SchemaError):
    pass 

class SchemaTypeMismatch(SchemaError, TypeError):
    pass 


def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    
    if missing_keys or extra_keys:
        missing_msg = (
            "missing keys: " + ",".join({path + "." + str(key) for key in missing_keys})
        )
        extras_msg = ('extra keys: ' + '.'.join({path + '.' + str(key) for key in extra_keys})) if extra_keys else ""
        raise SchemaKeyMismatch(''.join(missing_msg, extras_msg))
    else:
        return True, None
        

def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict 
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = (
                'incorrect type: ' + path + "." + key + 
                '-> expected' + template_type.__name__ + 
                ', found' + type(data_value).__name__
            )
            raise SchemaTypeMismatch(err_msg)
    return True, None 


t ={'a':int, 'b': int, 'c': int, 'd': {}}
d = {'a': 'wrong type', 'b':100, 'c': 200, 'd': {'wrong', 'type'}}
is_ok, err_msg= match_keys(d, t, 'some.path')
#print(is_ok, err_msg)
n = 'ateya'
#print(type(n))
#print(type(n).__name__)

t = {'a': int, 'b': str, 'c': {'d': int}}
d = {'a': 100, 'b': 'test', 'c': {'some': "value"}}

#match_types(d, t, 'some.path')

def recursive_validate(data, template, path):
    is_ok, err_msg = match_keys(data, template, path)
    if not is_ok:
        return False, err_msg
    
    is_ok, err_msg = match_types(data, template, path)
    if not is_ok:
        return False, err_msg

    dictonary_type_keys = {key for key, value in template.items() if isinstance(value, dict)}

    for key in dictonary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_ok, err_msg = recursive_validate(sub_data,sub_template, sub_path)
        if not is_ok:
            return False, err_msg

    return True, None 

def validate(data, template):
    return recursive_validate(data, template, '')

persons = ((John, 'John'), (Michael, 'Michael'))
for person, name in persons:
    is_ok, err_msg = validate(person, template)
    print(f'{name}: valid={is_ok}:{err_msg}')


def validate(data, template):
    is_ok, err_msg = recursive_validate(data, template, '')
    if not is_ok:
        raise SchemaError(err_msg)

try:
    for person, name in persons:
        validate(person, template)
except SchemaError as ex:
    print("Validation failed", str(ex))


try:
    validate(Eric, template)
except SchemaKeyMismatch as ex:
    print("handling a key mismatch exception", ex)
except SchemaTypeMismatch as ex:
    print('handling a type mismatch exception', ex)
except SchemaError as ex:
    print('handling some general schema exception', ex)
except TypeError as ex:
    print('handling a general type exception', ex)





#validate(John, template)
