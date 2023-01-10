
def splitShiftIntoList(shifts):
    shifts = shifts.split(",")
    shifts[0] = shifts[0].split("-")
    shifts[1] = shifts[1].split("-")
    return shifts


def isfullyContained(shift1, shift2):
    return (int(shift1[0]) <= int(shift2[0])) and (int(shift1[1]) >= int(shift2[1]))


def doesOverlap(shift1, shift2):
    lowerBoundWithin = (int(shift1[0]) <= int(shift2[0])) and (
        int(shift1[1]) >= int(shift2[0]))
    upperBoundWithin = (int(shift1[0]) <= int(shift2[1])) and (
        int(shift1[1]) >= int(shift2[1]))
    return lowerBoundWithin or upperBoundWithin


def main():
    f = open("input_day4.txt", "r")
    shifts = f.readlines()

    fullyContainedShifts = 0
    overlappedShifts = 0
    for shift in shifts:
        shiftList = splitShiftIntoList(shift)
        if isfullyContained(shiftList[0], shiftList[1]) or isfullyContained(shiftList[1], shiftList[0]):
            fullyContainedShifts += 1
        if doesOverlap(shiftList[0], shiftList[1]) or doesOverlap(shiftList[1], shiftList[0]):
            overlappedShifts += 1
    print(f"Number of fully contained shifts {fullyContainedShifts}")
    print(f"Number of overlapped shifts {overlappedShifts}")


if __name__ == "__main__":
    main()
