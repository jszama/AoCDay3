import string

file = open("input3.txt","r")
ruckSack = []
total = 0

for line in file:
    ruckSack.append(line.strip("\n"))

for item in ruckSack:
    half = len(item)//2
    
    leftSide = item[:half]
    rightSide = item[half:]
    
    # Value initially starts from zero so we tell it to start from 1
    for value, character in enumerate(string.ascii_letters, start=1):
        if character in leftSide and character in rightSide:
            total += value
            
print(total)
    
 # Part 2 
total = 0
currentCheck = 3

for i in range(0 , len(ruckSack), 3):
    currentData = ruckSack[i:currentCheck]
    
    for value, character in enumerate(string.ascii_letters, start=1):
        if character in currentData[0] and character in currentData[1] and character in currentData[2]:
            total += value

    currentCheck += 3
    
print(total)