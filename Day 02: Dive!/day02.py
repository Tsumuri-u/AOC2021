fileObject = open("input02.txt", "r")
data = fileObject.read()
data = data.split()

def part_one():
    horizontalPosition = 0
    depth = 0
    answer = 0
    
    i = 0
    while i < (len(data)):
        direction = data[i]
        toMove = int(data[i + 1])
        
        if direction == "forward":
            horizontalPosition += toMove
        elif direction == "up":
            depth -= toMove
        elif direction == "down":
            depth += toMove;
        i += 2
        
    answer = horizontalPosition * depth
    print("Part 1: " + str(answer))
    
def part_two():
    horizontalPosition = 0
    depth = 0
    aim = 0
    answer = 0  
    
    i = 0
    while i < (len(data)):
        direction = data[i]
        toMove = int(data[i + 1])
        
        if direction == "forward":
            horizontalPosition += toMove
            depth += (aim * toMove)
        elif direction == "up":
            aim -= toMove
        elif direction == "down":
            aim += toMove;
        i += 2
        
    answer = horizontalPosition * depth
    print("Part 2: " + str(answer))    
    
part_one()
part_two()