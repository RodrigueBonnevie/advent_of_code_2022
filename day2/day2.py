f = open("input_day2.txt","r")

def pointsForChoice(choice):
    match choice:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3
        case _:
            return 0 

def pointsForResult(elfsChoice, myChoice):
    match elfsChoice:
        case "A":
            match myChoice:
                case "A":
                    return 3
                case "B":
                    return 6
                case "C":
                    return 0
                case _:
                    return 0 
        case "B":
            match myChoice:
                case "A":
                    return 0
                case "B":
                    return 3
                case "C":
                    return 6
                case _:
                    return 0 
        case "C":
            match myChoice:
                case "A":
                    return 6
                case "B":
                    return 0
                case "C":
                    return 3
                case _:
                    return 0 
        case _:
            return 0 

def choiceFromOutcome(elfsChoice, outcome):
    match outcome:
        case "X": # Lose
            match elfsChoice:
                case "A":
                    return "C"
                case "B":
                    return "A"
                case "C":
                    return "B"
                case _:
                    return "" 
        case "Y": # Draw
            return elfsChoice
        case "Z": # Win
            match elfsChoice:
                case "A":
                    return "B"
                case "B":
                    return "C"
                case "C":
                    return "A"
                case _:
                    return "" 
        case _:
            return "" 


rounds = f.readlines()
totalPoints = 0
for round in rounds:
    myChoice = choiceFromOutcome(round[0],round[2])
    totalPoints += pointsForChoice(myChoice)
    totalPoints += pointsForResult(round[0], myChoice)

print(f"Total points for strategy {totalPoints}")