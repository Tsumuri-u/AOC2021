fileObject = open("input01.txt", "r")
data = fileObject.read()
data = data.split()

curr = -1
answer = 0

for i in range(len(data)):
    toInt = int(data[i])
    if curr >= 0 and toInt > curr:
        answer += 1
    curr = toInt
    
print(answer)