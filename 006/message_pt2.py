with open("006\input.txt") as file:
    line=file.readline()

    index=0
    for x in range(len(line)):
        if len(line) - 14 >= x:
            sub_string=line[x:x+14]

            if len(line[x:x+14]) == len(set(sub_string)):
                index=x+14
                break
    
    print(str(index))

