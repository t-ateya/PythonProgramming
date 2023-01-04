import yaml 

data = '''
---
title: Parrot Sketch
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - firs_name: Michael
      last_name: Palin
      dob: 1943-05-05
'''

d = yaml.load(data)
print(d)