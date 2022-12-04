import string
alphabet = list(string.ascii_lowercase)

with open("adventOfCode/003/input.txt") as file:
    total = 0
    line = file.readline()
    while line:
        a,b = line[:int(len(line)/2)], line[int(len(line)/2):]
        c = [ x for x in a if x in b ]
        
        try:
            d=alphabet.index(c[0])
            total+=d+1
        except:
            d=alphabet.index(str(c[0]).lower())
            total+=d+27
        line = file.readline()
    
    print(str(total))