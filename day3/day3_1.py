with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip() for temp in lines]
    lines = [[line[:int(len(line)/2)],line[int(len(line)/2):]] for line in lines]

    total_priority = 0
    dup_letters = []
    for line in lines:
        for letter in line[0]:
            if letter in line[1]:
                dup_letters.append(letter)
                break
                
    for letter in dup_letters:
        if letter.islower():
            total_priority += (ord(letter) - (ord('a')-1))
        else:
            total_priority += (ord(letter) - (ord('A')-1) + 26)
            
    print(total_priority)
    
