#open a file
file = open("example.txt", "r")
#read the contents of the file
content = file.read()
print(content)
#close the file
file.close()
# Writing to a file
file = open("example.txt", "a")
file.write("\nAdding a new line to the file.")
file.close()    

#file properties
f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)
