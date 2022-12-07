def f(cwd):
    total = 0
    if cwd["size"] <= 100000:
        total+=cwd["size"]
    for key in cwd["sub_nodes"]:
        total+=f(cwd["sub_nodes"][key])

    return total

main_dir = {
    "size" : 0,
    "sub_nodes" : {
    }
}
stack=[]
cwd = main_dir
with open("007\input.txt") as file:

    line = file.readline()
    while line:
        line = line.strip()
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5] == '/':
                    stack=[]
                    cwd = main_dir
                elif line[5] == '.':
                    temp_size = cwd["size"]
                    cwd = stack.pop()
                    cwd["size"] += temp_size
                else:
                    stack.append(cwd)
                    cwd = cwd["sub_nodes"][line[5:]]
        elif line[:3] == "dir":
            cwd["sub_nodes"][line[4:]] = {"size" : 0, "sub_nodes" : {}}
        else:
            a,b = line.split(" ")
            cwd["size"] += int(a)

        line = file.readline()
    
while len(stack)>0:
    temp_size = cwd["size"]
    cwd = stack.pop()
    cwd["size"] += temp_size

    
total = f(main_dir)

print(str(total))