import string
alphabet = list(string.ascii_lowercase)

t1,t2 ='',''
c=''
with open("adventOfCode/003/input.txt") as file:
    total = 0
    line = file.readline()
    while line:

        if t1 == '':
            t1 = line
        elif t2 == '':
            t2 = line
        else:
            for a in line:
                if a in t1 and a in t2:
                    c=a
                    break
            t1 = t2 = ''

            try:
                d=alphabet.index(c)
                total+=d+1
                c=''
            except:
                d=alphabet.index(c.lower())
                total+=d+27
                c=''

        line = file.readline()
    
    print(str(total))