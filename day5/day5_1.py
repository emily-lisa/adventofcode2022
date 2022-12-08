with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.replace('\n', '') for temp in lines]

    starting_state = []
    moves = []
    switch_read = 0
    for line in lines:
        if line == '':
            switch_read = 1
        else:
            if switch_read == 0:
                starting_state.append(line.replace('[', '').replace(']', '').replace('    ', ' ! ').replace('     ', ' ! ').split())
            elif switch_read == 1:
                moves.append(line.split())

    only_boxes = []
    
    for i in range(8):
        only_boxes.append(starting_state[i])

    only_boxes.reverse()


    stacks = []
    for i in range(9):
        stacks.append([])
        for y in range(8):
            if only_boxes[y][i] != '!':
                stacks[i].append(only_boxes[y][i])
        

    amount = 0
    start = 0
    destination = 0
    for line in moves:
        amount = int(line[1])
        start = int(line[3])-1
        destination = int(line[5])-1
        for i in range(amount):
            stacks[destination].append(stacks[start].pop())

    for stack in stacks:
        print(stack)
            


    