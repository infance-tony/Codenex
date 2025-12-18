# forloop
n = 4
for i in range(0, n):
    print(i)

# while loop
count = 0
while count < 5:            
    print(count)
    count += 1

# nested loop
for i in range(1, 4):                   
    for j in range(1, 4):               
        print(i, j)                             

#do-while loop simulation
count = 0
while True: 
    print(count)
    count += 1
    if not (count < 5):
        break
    
# break , pause, contine , jump statements
for i in range(10):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        break     # Exit the loop when i is 7
    print(i)
else:
    print("Loop completed without break")
print("Loop ended.")

for i in range(5):
    print(i)
    if i == 2:
        pass  # Placeholder, does nothing
print("Loop finished.")
for i in range(5):
    if i == 3:
        print("Jumping to next iteration")
        continue  # Jump to the next iteration when i is 3
    print(i)
print("Loop ended.")







