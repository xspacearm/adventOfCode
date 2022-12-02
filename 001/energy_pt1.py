with open("001\input.txt","r") as file:
    contents = file.readlines()

mostEnergy = 0
sum = 0
elves = 0
for energy in contents:
    if energy != '\n':
        energy.replace('\n','')
        sum += int(energy)
    else:
        elves+=1
        if mostEnergy < sum:
            mostEnergy=sum
        sum=0

print("Highest amount of energy: " + str(mostEnergy))
print("Total number of elves: " + str(elves))