with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip().split(',') for temp in lines]
    lines = [[temp[0].split('-'),temp[1].split('-')] for temp in lines]

    total = 0
    for line in lines:
        if int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1]):
            total += 1
        elif int(line[1][0]) >= int(line[0][0]) and int(line[1][1]) <= int(line[0][1]):
            total += 1

    print(total)