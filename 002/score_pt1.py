with open("002\input.txt") as file:
    total = 0
    line = file.readline()
    while line:
        if line[0] == 'A':
            if line[2] == 'X':
                total+=4
            elif line[2] == 'Y':
                total+=8
            elif line[2] == 'Z':
                total+=3
        elif line[0] == 'B':
            if line[2] == 'X':
                total+=1
            elif line[2] == 'Y':
                total+=5
            elif line[2] == 'Z':
                total+=9
        elif line[0] == 'C':
            if line[2] == 'X':
                total+=7
            elif line[2] == 'Y':
                total+=2
            elif line[2] == 'Z':
                total+=6
        line = file.readline()
    print(str(total))
