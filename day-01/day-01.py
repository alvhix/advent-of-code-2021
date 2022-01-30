# Part 1: count increases from previous value (the first value does not have previous value)
def count_increases(arr):
    counter = 0
    prev_element = None

    for element in arr:

        if prev_element != None and element > prev_element:
            counter += 1
        prev_element = element

    return counter


# setup
file = open("input.txt", "r")
arr = [int(i) for i in file.read().split("\n")]
file.close()

print(count_increases(arr))
