# part 1
def calculate_position(arr):
    horizontal = 0
    depth = 0
    for i in arr:
        if i[0] == "forward":
            horizontal += i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "up":
            depth -= i[1]

    return horizontal * depth


# setup
file = open("input.txt", "r")
# list of lists of instruction (string) and value (integer)
# [['forward', 3], ['down', 6], ['up', 2]]
arr = [i.split(" ") for i in file.read().split("\n")]
for i in range(0, len(arr)):
    arr[i] = [arr[i][0], int(arr[i][1])]
file.close()

print(calculate_position(arr))
