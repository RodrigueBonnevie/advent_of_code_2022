f = open("input_day2.txt","r")

def pointsForChoice(choice):
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
        case _:
            return 0 

def pointsForResult(elfsChoise, myChoice):
    match elfsChoise:
        case "A":
            match myChoice:
                case "X":
                    return 3
                case "Y":
                    return 6
                case "Z":
                    return 0
                case _:
                    return 0 
        case "B":
            match myChoice:
                case "X":
                    return 0
                case "Y":
                    return 3
                case "Z":
                    return 6
                case _:
                    return 0 
        case "C":
            match myChoice:
                case "X":
                    return 6
                case "Y":
                    return 0
                case "Z":
                    return 3
                case _:
                    return 0 
        case _:
            return 0 


rounds = f.readlines()
totalPoints = 0
for round in rounds:
    totalPoints += pointsForChoice(round[2])
    totalPoints += pointsForResult(round[0], round[2])

print(f"Total points for strategy {totalPoints}")