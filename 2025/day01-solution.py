def solution1():
    with open("day01-input.txt", "r") as file:
        lines = file.readlines()

    count = 0
    position = 50
    for line in lines:
        direction = line[0]
        rotations = int(line[1:].strip()) % 100
        if direction == "L":
            # decreases number values <-
            position = (position - rotations + 100) % 100
        elif direction == "R":
            position = (position + rotations) % 100

        # check position after rotation
        if position == 0:
            count += 1

    print(count)


def solution2():
    with open("day01-input.txt", "r") as file:
        lines = file.readlines()

    count = 0
    position = 50
    for line in lines:
        direction = line[0]
        rotations = int(line[1:].strip())
        ## full spin will always pass through 0
        fullSpins = rotations // 100
        count += fullSpins
        ## remaining rotations pass/end on 0
        remainder = rotations % 100
        start = position
        if direction == "L":
            # decreases number values <-
            position = (position - remainder + 100) % 100
            if (position > start) and (start != 0) and (position != 0):
                count += 1
        elif direction == "R":
            position = (position + remainder) % 100
            if (position < start) and (start != 0) and (position != 0):
                count += 1

        # check position after rotation
        if position == 0:
            count += 1

    print(count)


solution2()
