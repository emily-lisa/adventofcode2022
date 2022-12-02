with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [temp.strip().split() for temp in lines]
    score = 0
    for line in lines:
        match line[0]:
            case 'A':
                match line[1]:
                    case 'X':
                        score += 3
                        score += 1
                    case 'Y':
                        score += 6
                        score += 2
                    case 'Z':
                        score += 0
                        score += 3
            case 'B':
                match line[1]:
                    case 'X':
                        score += 0
                        score += 1
                    case 'Y':
                        score += 3
                        score += 2
                    case 'Z':
                        score += 6
                        score += 3
            case 'C':
                match line[1]:
                    case 'X':
                        score += 6
                        score += 1
                    case 'Y':
                        score += 0
                        score += 2
                    case 'Z':
                        score += 3
                        score += 3
    print(score)