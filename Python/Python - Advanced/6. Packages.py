#packahges example
import os
import sys
#using os module
print("Current Working Directory:", os.getcwd())
print("List of files and directories in current directory:", os.listdir('.'))
#using sys module
print("Python version:", sys.version)
print("Platform:", sys.platform)
#creating a package
# Assuming we have a package named 'mypackage' with a module 'mymodule.py' containing a function 'hello()'
from mypackage.mymodule import hello
hello()  # calling the function from the custom package module
# To create the package structure, you would have:
# mypackage/
# ├── __init__.py
# └── mymodule.py
# And in mymodule.py, you would define the hello function:
# def hello():
#     print("Hello from mymodule in mypackage!")    
# Note: The above package structure and function definition are for illustration purposes only and should be created in separate files for actual use.