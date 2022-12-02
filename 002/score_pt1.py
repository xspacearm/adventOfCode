with open("002\input.txt") as file:
    total = 0
    line = file.readline()
    while line:
        a,b = line.split()
        a="ABC".index(a)
        b="XYZ".index(b)
        total+=(b+1)

        if(a-b)==0:
            total+=3
        elif(a-b)==-1 or (a-b)==2:
            total+=6
                
        line = file.readline()
    print(str(total))
