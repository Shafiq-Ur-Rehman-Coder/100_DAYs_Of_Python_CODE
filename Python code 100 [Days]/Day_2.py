# =========================================
# Chapter 2: Variables and Data Types
# =========================================

# A variable is a name used to store data
# Data can be number, text, True/False, or empty

# INTEGER (int)
# int is used for WHOLE numbers
# Whole numbers means NO decimal point
# Examples: 1, 5, 12, 100, 0
age = 12
print(age)                  # Output: 12
print(type(age))            # Output: <class 'int'>

# FLOAT (float)
# float is used for numbers WITH decimal point
# Examples: 1.5, 2.3, 3.14, 10.0
height = 5.6
print(height)               # Output: 5.6
print(type(height))         # Output: <class 'float'>

# STRING (str)
# str is used for text, words, or sentences
# Text must be inside ' ' or " "
name = "Ali"
print(name)                 # Output: Ali
print(type(name))           # Output: <class 'str'>

# BOOLEAN (bool)
# bool is used for True or False
# True means YES, False means NO
is_student = True
print(is_student)           # Output: True
print(type(is_student))     # Output: <class 'bool'>

# NONE TYPE (None)
# None means no value or empty
result = None
print(result)               # Output: None
print(type(result))         # Output: <class 'NoneType'>

# CHANGING VARIABLE VALUE
# Variable value can change anytime
score = 10
print(score)                # Output: 10
score = 20
print(score)                # Output: 20

# MULTIPLE VARIABLES
# Assign many values in one line
a, b, c = 1, 2, 3
print(a, b, c)              # Output: 1 2 3

# USING VARIABLES IN PRINT
language = "Python"
version = 3
print("Language:", language)   # Output: Language: Python
print("Version:", version)    # Output: Version: 3

# F-STRING
# f-string is the easiest way to print variables
print(f"{language} version {version}")
# Output: Python version 3



# -------------------------------------------
cl = input("enter your class> ")
marks = int(input("enter your marks> "))
name = input("enter your name> ")
student = input("enter that you studen are> ")
print(f"you got marks {marks} and your name is  {name}  and you are {student} in class {cl}")