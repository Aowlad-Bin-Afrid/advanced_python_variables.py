# =========================================
# Advanced Python Variables Tutorial
# =========================================

# 1. What is a Variable?
# A variable is a name that stores data in memory.
# It can hold different data types like numbers, strings, lists, etc.

# Basic examples
name = "Arafat"          # string
age = 25                 # integer
height = 5.9             # float
is_student = True        # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# -----------------------------------------
# 2. Multiple Assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Swapping variables
x, y = y, x
print("After swap - x:", x, "y:", y)

# -----------------------------------------
# 3. Variable Types and Type Conversion
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>

# Type conversion
age_str = str(age)
print("Age as string:", age_str, type(age_str))

height_int = int(height)  # Converts float to int (truncates decimal)
print("Height as int:", height_int)

# -----------------------------------------
# 4. Constants (by convention)
# Python does not have real constants, but by convention, uppercase names indicate constants
PI = 3.14159
GRAVITY = 9.8
print("PI:", PI, "Gravity:", GRAVITY)

# -----------------------------------------
# 5. Global vs Local Variables

global_var = "I am global"

def variable_scope():
    local_var = "I am local"
    print(global_var)   # Can access global variable
    print(local_var)    # Can access local variable

variable_scope()
# print(local_var)      # This would give an error, because local_var is not global

# Modifying global variable inside a function
def modify_global():
    global global_var
    global_var = "I am modified global"

modify_global()
print(global_var)

# -----------------------------------------
# 6. Dynamic Typing
# Python variables can change type during runtime
data = 100         # integer
print(data, type(data))

data = "Now I am string"  # changed to string
print(data, type(data))

# -----------------------------------------
# 7. Variable Naming Rules
# - Must start with a letter or underscore
# - Can contain letters, numbers, underscores
# - Case-sensitive: age and Age are different
# - Cannot use Python reserved keywords (if, for, while, etc.)

# Good examples
my_var = 10
_userName = "Coco"
data2 = 55

# Bad examples (will cause errors)
# 2data = 100
# user-name = "error"

# -----------------------------------------
# 8. Input from User and Variables
user_input = input("Enter your favorite programming language: ")
print("You like", user_input)

# -----------------------------------------
# 9. Advanced Concepts with Variables

# a) Multiple types in one variable
my_list = [1, "two", 3.0, True]
print("List:", my_list)

# b) Variable referencing (assignment does not copy for mutable types)
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print("list1:", list1)  # list1 is also modified
print("list2:", list2)

# To avoid this, use copy
import copy
list3 = copy.deepcopy(list1)
list3.append(5)
print("list1 after deepcopy:", list1)
print("list3 after deepcopy:", list3)

# c) Constants using typing.Final (Python 3.8+)
from typing import Final
MAX_USERS: Final = 100
print("Max Users:", MAX_USERS)