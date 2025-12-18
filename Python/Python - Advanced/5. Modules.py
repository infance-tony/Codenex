#modules example
import math
import random
#using math module
print("Square root of 16 is:", math.sqrt(16))
print("Value of pi is:", math.pi)
#using random module
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

#creating a custom module
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
