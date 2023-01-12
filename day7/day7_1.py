with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]

    #print(lines)

    dir_tree = []
    dir_size = []
    dir_tree.append("main")
    current_dir = ''
    current_size = 0
    x = 0
    y = 0


    for line in lines:
        if line[0] == '$':
            match line[2]:
                case 'c':
                    if line[5] == '.':
                        y -= 1
                    else:
                        y += 1
                        print(current_size)
                        line = line.split()
                        current_dir = line[2]
                        dir_tree.append(current_dir)
                        dir_size.append(current_size)
                        current_size = 0
                        
                        


                #case 'l':
        
        elif line[0] == 'd':
            print(line)

        else:
            line = line.split()
            current_size += int(line[0])


    dir_size.append(current_size)

    total = 0

    for i in range(len(dir_tree)):
        print(dir_tree[i])
        print(dir_size[i])
        if dir_size[i] <= 100000:
            total += dir_size[i]
        print("______")


    print(total)