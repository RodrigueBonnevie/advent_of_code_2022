def splitBackpackIntoCompartment(backpack):
    middle = int((len(backpack)-1)/2)  # -1 because of \n
    compartments = [backpack[:middle], backpack[middle:]]
    return compartments


def findCommonLetterInCompartments(compartment1, compartment2):
    for letter in compartment1:
        letterPosition = compartment2.find(letter)
        if letterPosition != -1:
            return letter
    return ""


def calculateItemPriority(item):
    asciiNumber = ord(item)
    if item.isupper():
        return asciiNumber - 65 + 27
    else:
        return asciiNumber - 96


def findCommonLetterInBackpacks(backpack1, backpack2, backpack3):
    for letter in backpack1:
        letterPosition2 = backpack2.find(letter)
        if letterPosition2 != -1:
            letterPosition3 = backpack3.find(letter)
            if letterPosition3 != -1:
                return letter
    return ""


def main():
    f = open("input_day3.txt", "r")
    backpacks = f.readlines()

    itemSum = 0
    for backpack in backpacks:
        compartments = splitBackpackIntoCompartment(backpack)
        item = findCommonLetterInCompartments(compartments[0], compartments[1])
        itemSum += calculateItemPriority(item)

    badgeSum = 0
    for i in range(0, len(backpacks)-2, 3):
        badge = findCommonLetterInBackpacks(
            backpacks[i], backpacks[i+1], backpacks[i+2])
        badgeSum += calculateItemPriority(badge)

    print(f"Priority sum of items {itemSum}")
    print(f"Priority sum of badges {badgeSum}")


if __name__ == "__main__":
    main()
