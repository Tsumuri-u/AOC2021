fileObject = open("input03.txt", "r")
data = fileObject.read()

def part_one():
    gammaRate = ""
    epsilonRate = ""
    answer = 0
    
    for i in range(12):
        zeroCount = 0
        oneCount = 0
        
        j = i
        while j < len(data):
            if int(data[j]) == 0:
                zeroCount+=1
            elif int(data[j]) == 1:
                oneCount+=1
            j += 13
        
        if zeroCount >= oneCount:
            gammaRate += "0"
        elif oneCount > zeroCount:
            gammaRate += "1"
    
    for i in range(len(gammaRate)):
        if gammaRate[i] == "0":
            epsilonRate += "1"
        elif gammaRate[i] == "1":
            epsilonRate += "0"
            
    answer = (int(gammaRate, 2)) * (int(epsilonRate, 2))
    print("Part 1: " + str(answer))
    
def part_two():
    array = data.split()
    
    for i in range(12):
        
        j = i
        while j < len(data):
            
            j += 13

part_one()
part_two()
