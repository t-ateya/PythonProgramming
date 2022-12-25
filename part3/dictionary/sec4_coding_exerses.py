"""
    Coding Exercises


================Exercise 1   ===================
    Write a Python that will create and return a dictionary from  another dictionary, but sorted by value. You can assume the values are
    all comparable and have a natural sort order

    For example,
    given the following dictionary:
    composers = {'Johann' : 65, 'Ludwig': 56, 'Frederic' : 39, 'Wolfgang': 35}

    Your function should return a dictionary that looks like the following

    sorted_composers = {
        'Wolfgang' : 35,
        'Frederic' : 39,
        'Ludwig' : 56,
        'Jonhson' : 65
    }

    Hint: you'll likely want to use python's sorted function


============= Exercise 2 ===================================
Given two dictinaries, d1 and d2, write a function that creates a dictionary that contains only the keys common to both dictionaries, with values
being a tuple containing the values from d1 and d2. (Order of keys is not important)

For example, given two dictionaries as follows:
d1 = {'a' :1, 'b': 2, 'c' : 3, 'd' : 4}
d2 = {'b' : 20, 'c' : 30, 'y' : 40, 'z' : 50}

Your function should return a dictionary that looks like this:
d = {'b' : (2, 20), 'c': (3, 30)}

Hint: Remember that s1 & s2 will return the intersection of two sets.
Again, try to keep your code pythonic - don't just start with an empty dictionary and build it up one by one-think of a cleaner approach


=============== Exercise 3 ===================================
You have text data spread across multiple servers. Each server is able to analyse this data and return a dictionary that contains words and their
frequency.
Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data
source. Bonus points if you can make your dictionary sorted by frequency(highest to lowest) 

For example, you may have three servers that each return these dictionaries:

d1 = {'python': 10, 'java':3, 'c#": 8, 'javascript' : 15}
d2 = {'java': 10, 'c++':10, 'c#": 4, 'go' : 9, 'python' : 6}
d3 = {'erlang': 5, 'haskell':2, 'python": 1, 'pascal' : 1}

Your resulting dictionary should look like:

d = {
    'python' : 17,
    'javascript' : 15,
    'java' : 13,
    'c#' : 12,
    'c++' : 10,
    'go' : 9,
    'erlang' : 5,
    'haskell' : 2,
    'pascal' : 1
}

if only servers 1 and 2 return data (so d1 and d2), your result would look like:
d = {
    'python' : 16,
    'javascript' : 15,
    'java' : 13,
    'c#' : 12,
    'c++': 10,
    'go' : 9
}



============= Exercise 4 ===================
For this exercise, suppose you have a web API load balanced across multiple nodes. This API receives various requests for resources and logs each request to 
some local storage. Each instane of the API is able to return a dictionary containing the resource that was accessed(the dictionary key) and the number of times
it was requested(the associated values)

Your task here is to identify resources that have been requested on some, but not all the servers, so you can determine if you have an issue with your load
balancer not distributing certain resource requests across all nodes.

For simplicity, we will assume that there are exactly 3 nodes in the cluster.

You should write a function that takes 3 dictionaries as arguement for node1, node2, and node 3, and returns a dictionary that contains only keys that are not found
in all the dictionaries. The value should be a list containing the number of times it was requested in each node (The node order should match the dictionary(node)
order passed to your function). Use 0 if the resource was not requested from the corresponding node.

Suppose your dictionaries are for logs of all the GET requests on each node:

n1 = {'employees': 100, 'employee' : 5000, 'users' : 10, 'user' : 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}
 
  Your result should then be:
   result = {
                'employee' : (5000, 0, 0),
                'user' : (100, 230, 0),
                'login' : (0, 0, 1000)
   }
Tip: to find the difference between two sets, you can subtract one from the other:

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3}
s1 - s2

Tip: To get the union of two (or more) sets you can use the | operator.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2

Tip: To get the intersection of two (or more) sets you can use the & operator.
s1 = {1, 2, 3, 4}
s2 = {2, 3}
s1 & s2

"""

#=====================Exercise 1 solution ==============================================
composers = {'Johann' : 65, 'Ludwig': 56, 'Frederic' : 39, 'Wolfgang': 35}
#sorted_composers = {k:v for k, v in sorted(composers.items(), key=lambda item : item[1])}

def sort_dict_by_value(d):
    sorted_dict = {k : v for k, v in sorted(d.items(), key = lambda item : item[1])}
    return sorted_dict

def sorted_dict_method2(d):
    return dict(sorted(d.items(), key=lambda item : item[1]))

sorted_composers = sort_dict_by_value(composers)
#print(sorted_composers)

#print(sorted_dict_method2(composers))


# ===================== Exercise 2 Solution =======================
def common_keys_dict(d1, d2):
    """Returns the keys common to both dictionaries"""
    common_keys = d1.keys() & d2.keys()
    common_dic = {k : (d1[k], d2[k]) for k in common_keys}
    return common_dic

d1 = {'a' :1, 'b': 2, 'c' : 3, 'd' : 4}
d2 = {'b' : 20, 'c' : 30, 'y' : 40, 'z' : 50}

#print(common_keys_dict(d1, d2))

# =================== Exercise 3 Solution =======================

d1 = {'python': 10, 'java':3, "c#": 8, 'javascript' : 15}
d2 = {'java': 10, 'c++':10, "c#": 4, 'go' : 9, 'python' : 6}
d3 = {'erlang': 5, 'haskell':2, "python": 1, 'pascal' : 1}

def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            if k not in unsorted.keys():
                unsorted[k] = v
            else:
                unsorted[k] += v
    sorted_dict = dict(sorted(unsorted.items(), key= lambda item : item[1], reverse=True))
    return sorted_dict

def merge_approach2(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v 
    sorted_dic = {k : v for k, v in sorted(unsorted.items(), key = lambda x: x[1], reverse=True)}
    return sorted_dic

#print(merge(d1, d2, d3))
#print(merge_approach2(d1, d2, d3))


# ======================= Exercise 4 Solution ==================

n1 = {'employees': 100, 'employee' : 5000, 'users' : 10, 'user' : 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

def indentify(node1 :dict, node2:dict, node3:dict):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    uncommon_keys = union - intersection 
    result = {k : (node1.get(k, 0), node2.get(k, 0), node3.get(k, 0)) for k in uncommon_keys}
    return result

def generic_identify(*dicts):
    if len(dicts) <= 1:
        return None 
    keys = {}
    for _ in range(len(dicts)):
        for d in dicts:
            for k, v in d.items():
                keys[k] = {v}
    return keys

print(generic_identify(n1, n2, n3))
#print(indentify(n1, n2, n3))

