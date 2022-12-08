with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]

    line = lines[0]

    letter_buffer = []

    for i in range(len(line)):
        if len(letter_buffer) == 4:
            if len(set(letter_buffer)) == 4:
                print(letter_buffer)
                print(i)
            else:
                letter_buffer.pop(0)
        letter_buffer.append(line[i])
