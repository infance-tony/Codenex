# Python String - Complete Guide with Examples

# 1. Creating a String
print("=== Creating Strings ===")
s1 = 'GfG'  # single quote
s2 = "GfG"  # double quote
print(s1)
print(s2)

# 2. Multi-line Strings
print("\n=== Multi-line Strings ===")
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

# 3. Accessing Characters in String
print("\n=== Accessing Characters ===")
s = "GeeksforGeeks"
print(f"First character: {s[0]}")
print(f"5th character: {s[4]}")

# Negative indexing
print(f"3rd character from start: {s[-10]}")
print(f"5th character from end: {s[-5]}")

# 4. String Slicing
print("\n=== String Slicing ===")
s = "GeeksforGeeks"
print(f"Characters from index 1 to 3: {s[1:4]}")
print(f"From start to index 2: {s[:3]}")
print(f"From index 3 to end: {s[3:]}")
print(f"Reverse string: {s[::-1]}")

# 5. String Iteration
print("\n=== String Iteration ===")
s = "Python"
for char in s:
    print(char)

# 6. String Immutability
print("\n=== String Immutability ===")
s = "geeksforGeeks"
s = "G" + s[1:]  # create new string
print(f"Modified string: {s}")

# 7. Deleting a String
print("\n=== Deleting a String ===")
s = "GfG"
print(f"Before deletion: {s}")
del s
# print(s)  # This would cause NameError

# 8. Updating a String
print("\n=== Updating a String ===")
original = "Hello World"
updated = original.replace("World", "Python")
print(f"Original: {original}")
print(f"Updated: {updated}")

# Additional string operations
updated2 = original.upper()
print(f"Uppercase: {updated2}")

updated3 = original.lower()
print(f"Lowercase: {updated3}")