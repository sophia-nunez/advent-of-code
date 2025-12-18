def solution1():
    with open("day03-input.txt", "r") as file:
        lines = file.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        first = -1
        second = -1
        # go through bank and find max values
        for i in range(len(line)):
            num = (int)(line[i])
            # larger first value AND we have at least one value following
            if (num > first) and (i < len(line) - 1):
                first = num
                second = (int)(line[i + 1])
            # not larger than first, check for second
            elif num > second:
                second = num

        # add the joltage to sum
        sum += (first * 10) + second

    print(sum)


def solution2():
    with open("day03-input.txt", "r") as file:
        lines = file.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        for i in range(12):
            # need at least this many indices after our selected value
            remaining = 11 - i
            value = int(line[0])
            index = 0
            for j in range(1, len(line) - remaining):
                num = int(line[j])
                if num > value:
                    index = j
                    value = num
            # add current digit to sum
            sum += value * (10**remaining)
            # cut earlier digits from line
            line = line[index + 1 :]

    print(sum)


solution2()
