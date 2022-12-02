with open("001\input.txt","r") as file:
    contents = file.readlines()

energyList = []
sum = 0
elves = 0
for energy in contents:
    if energy != '\n':
        energy.replace('\n','')
        sum += int(energy)
    else:
        elves+=1
        energyList.append(sum)
        sum=0

energyList.sort(reverse=True)
sumOfEnergy = energyList[0] + energyList[1] + energyList[2]
print("Highest amount of energy: " + str(sumOfEnergy))
print("Total number of elves: " + str(elves))