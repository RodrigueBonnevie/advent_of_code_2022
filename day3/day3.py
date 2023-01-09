def splitBackpackIntoCompartment(backpack):
    middle = int((len(backpack)-1)/2)  # -1 because of \n
    compartments = [backpack[:middle], backpack[middle:]]
    return compartments


def findCommonLetterInStrings(string1, string2):
    for letter in string1:
        letterPosition = string2.find(letter)
        if letterPosition != -1:
            return letter
    return ""


def calculateItemPriority(item):
    asciiNumber = ord(item)
    if item.isupper():
        return asciiNumber - 65 + 27
    else:
        return asciiNumber - 96


def main():
    f = open("input_day3.txt", "r")
    backpacks = f.readlines()

    prioritySum = 0
    for backpack in backpacks:
        compartments = splitBackpackIntoCompartment(backpack)
        item = findCommonLetterInStrings(compartments[0], compartments[1])
        prioritySum += calculateItemPriority(item)

    print(prioritySum)


if __name__ == "__main__":
    main()
