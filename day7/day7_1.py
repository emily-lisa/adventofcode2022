with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]

    print(lines)

    dir_tree = []
    dir_size = []
    current_dir = ''
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
                        line.split()
                        if len(dir_tree[y]) < x:
                            dir_tree[y].insert(x, line[2])
                        else:
                            dir_tree[y] = line[2]
                        


                case 'l':
        
        elif line[0] == 'd':

        else:
            line.split()
            += int(line[0])