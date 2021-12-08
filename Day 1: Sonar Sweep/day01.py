fileObject = open("input01.txt", "r")
data = fileObject.read()
data = data.split()

def part_one():
    curr = -1
    answer = 0

    for i in range(len(data)):
        toInt = int(data[i])
        if curr >= 0 and toInt > curr:
            answer += 1
        curr = toInt
        
    print("Part 1: " + str(answer))
    
def part_two():
    currWindow = -1
    answer = 0
    for i in range(len(data) - 2):
        tempWindow = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
        if currWindow >= 0 and tempWindow > currWindow:
            answer += 1;
        currWindow = tempWindow
    print("Part 2: " + str(answer))
    
part_one()
part_two()