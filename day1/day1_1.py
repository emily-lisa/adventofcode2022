with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]

    listOfElves = []
    y = 0
    listOfElves.append(0)
    for line in lines:
        if line == '':
            listOfElves.append(y)
            y = 0
        else:
            y += int(line)

    listOfElves.sort(reverse=True)
    print(listOfElves[0])
