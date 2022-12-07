def f(cwd,min,max):
    
    for key in cwd["sub_nodes"]:
        max = f(cwd["sub_nodes"][key], min, max)

    if cwd["size"] >= min and cwd["size"] <= max:
        max = cwd["size"]
        
    return max

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

min=30000000-(70000000-main_dir["size"])
total = f(main_dir, min,70000000)

print(str(total))