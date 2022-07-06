print("Hello World 😂")
print("*" * 10)

# press ctrl alt n to use code runner
age: int = 100
print(id(age))

x = [1, 2, 3]

# Strings are immutable
course = "Python Programming"
print(id(course))
print(id(course[0]))

# Escape Sequences
# \"
# \'
# \\
# \n

message = "Python \"Prgramming"
print(message)

new_message = """
      Python is one the most important languages
  I love programmin in python
"""
print(new_message)

# Formatted String
first = "Mosh"
last = "Hamedani"
full_name = f"{first} {last} is great programmer"
full_name = f"{len(first)} {2+2} is great programmer"
print(full_name)

# Remove wide space: strip()
#rstrip() or lstrip()

print("stripped message: ", new_message.strip())

#Find and replace
print(new_message.find("Pyth"))
print(new_message.replace("Pyth", "-"))
print("Programming" in new_message)
print("Programming" not in new_message)

