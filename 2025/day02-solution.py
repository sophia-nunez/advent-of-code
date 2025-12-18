import math


def solution1():
    with open("day02-input.txt", "r") as file:
        for line in file:
            range_list = line.strip().split(",")

    sum = 0
    for raw_range in range_list:
        values = raw_range.split("-")
        low = (int)(values[0])
        high = (int)(values[1])

        for i in range(low, high + 1):
            numDigits = math.floor(math.log10(i)) + 1
            if numDigits % 2 != 0:
                # can't repeat sequence if not even num digits
                continue
            # gets value to get first and second half using // and %
            separator = 10 ** (numDigits // 2)
            if (i // separator) == (i % separator):
                sum += i

    print(sum)


def solution2():
    with open("day02-input.txt", "r") as file:
        for line in file:
            range_list = line.strip().split(",")

    sum = 0
    for raw_range in range_list:
        values = raw_range.split("-")
        low = (int)(values[0])
        high = (int)(values[1])

        for i in range(low, high + 1):
            numDigits = math.floor(math.log10(i)) + 1
            # from single repeats to pairs, triples, etc.
            for j in range(1, numDigits // 2 + 1):
                if numDigits % j != 0:
                    # can't repeat sequence if not exact num of groupings
                    continue
                # compare each grouping of j digits
                curr = i
                separator = 10**j
                sequence = curr % separator
                while curr > 0:
                    if (curr % separator) != sequence:
                        separator = -1
                        break
                    curr //= separator
                # if no invalid sequence in current grouping, add to sum
                # also exit loop for current i (already found invalid group)
                if separator != -1:
                    sum += i
                    break

    print(sum)


solution2()
