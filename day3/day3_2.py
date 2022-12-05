with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]

    total_priority = 0
    dup_letters = []
    temp_one = ""
    temp_two = ""
    counter = 0
    for line in lines:
        match counter:
            case 0:
                temp_one = line
                counter += 1
            case 1:
                temp_two = line
                counter += 1
            case 2:
                for letter in line:
                    if letter in temp_one and letter in temp_two:
                        dup_letters.append(letter)
                        counter = 0
                        break

    print(len(dup_letters))
                
    for letter in dup_letters:
        if letter.islower():
            total_priority += (ord(letter) - (ord('a')-1))
        else:
            total_priority += (ord(letter) - (ord('A')-1) + 26)
            
    print(total_priority)
    
