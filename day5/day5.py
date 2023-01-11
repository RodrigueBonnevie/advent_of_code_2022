class CargoShip:
    def __init__(self, stateList):
        stateList.pop()  # Last element is the stack index, not needed here
        numberOfStacks = len(stateList[0]) // 4
        self.stacks = [[]for i in range(numberOfStacks)]
        for line in stateList:
            for stack in range(0, len(line)-1, 4):  # Each stack is 4 characters long
                stackNumber = stack // 4
                cargo = line[stack + 1]
                if cargo != " ":
                    self.stacks[stackNumber].insert(0, cargo)

    def moveCargo(self, numberOfCargoToMove, sourceStack, destinationStack):
        tmpStack = []
        for move in range(numberOfCargoToMove):
            tmpStack.insert(0, self.stacks[sourceStack].pop())

        for cargo in tmpStack:
            self.stacks[destinationStack].append(cargo)

    def printTopOfStacks(self):
        stackTops = ""
        for stack in self.stacks:
            stackTops += stack[-1]
        return stackTops


def main():
    initialStateList = []
    initialStateRead = False
    with open("input_day5.txt", "r") as inputFile:
        for line in inputFile.readlines():
            if line == "\n":  # empty line separates initial state and inputs
                cargoShip = CargoShip(initialStateList)
                initialStateRead = True
                continue

            if not initialStateRead:
                initialStateList.append(line)
            else:
                lineList = line.split(" ")
                numberOfCargoToMove = int(lineList[1])
                # Stacks in input are one indexed
                sourceStack = int(lineList[3]) - 1
                destinationStack = int(lineList[5]) - 1
                cargoShip.moveCargo(numberOfCargoToMove,
                                    sourceStack, destinationStack)
    print(cargoShip.printTopOfStacks())


if __name__ == "__main__":
    main()
