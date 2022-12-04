with open("adventOfCode/004/input.txt") as file:
    total = 0
    line = file.readline()
    while line:
        a1,b1=line.split(",")
        a1,a2=a1.split("-")
        b1,b2=b1.split("-")

        if (int(a1)<=int(b1) and int(a2)>=int(b1)) or (int(b1)<=int(a1) and int(b2)>=int(a1)):
            total+=1

        line = file.readline()
    
    print(str(total))