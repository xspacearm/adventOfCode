with open("002\input.txt") as file:
    total = 0
    line = file.readline()
    while line:
        a,b=line.split()
        a="ABC".index(a)
        b="XYZ".index(b)

        total+=b*3

        if b==1:
            total+=(a+1)
        else:
            total+=(a+(-1+b))%3+1

        line = file.readline()
    print(str(total))
