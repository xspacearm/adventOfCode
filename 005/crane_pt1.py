stacks_list = [[],[],[],[],[],[],[],[],[]]
with open("005\input.txt") as file:

    line = file.readline()
    while line:
        if line[0] != ' ' and line.strip() and 'move' not in line:
            for i in range(9):
                crate = line[(i+1) * 4 - 3]
                if crate != '' and crate != ' ' and not crate.isnumeric():
                    stacks_list[i].append(crate)
        elif 'move' in line:
            a = line.split(' ')
            for x in range(int(a[1])):
                stacks_list[int(a[5])-1].insert(0,stacks_list[int(a[3])-1].pop(0))
                
        line = file.readline()

final = ""
for x in range(9):
    final += str(stacks_list[x][0])
print(final)
