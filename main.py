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
    