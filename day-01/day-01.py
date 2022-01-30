# part 1
def count_increases(arr):
    counter = 0
    prev_element = None

    for element in arr:

        if prev_element != None and element > prev_element:
            counter += 1
        prev_element = element

    return counter


# part 2
def count_grouped_increases(arr):
    counter = 0
    sum_prev = None
    sum_actual = None

    for i in range(1, len(arr) - 1):

        sum_actual = arr[i - 1] + arr[i] + arr[i + 1]

        if sum_prev != None and sum_actual > sum_prev:
            counter += 1

        sum_prev = sum_actual

    return counter


# setup
file = open("input.txt", "r")
# list of integers
arr = [int(i) for i in file.read().split("\n")]
file.close()

print(count_increases(arr))
print(count_grouped_increases(arr))
