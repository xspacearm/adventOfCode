with open("006\input.txt") as file:
    line=file.readline()

    index=0
    for x in range(len(line)):
        if len(line) - 4 >= x:
            sub_string=line[x:x+4]

            if len(line[x:x+4]) == len(set(sub_string)):
                index=x+4
                break
    
    print(str(index))

