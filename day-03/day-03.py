# part 1
def calculate_power_consumption(arr):
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(0, len(arr[0])):
        zeros = 0
        ones = 0
        for element in arr:
            if element[i] == "0":
                zeros += 1
            elif element[i] == "1":
                ones += 1
        if zeros > ones:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate)


# from string binary to decimal integer
def binary_to_decimal(binary):
    decimal = 0
    for i in range(0, len(binary)):
        # 10110: 1 * 2^4 + 0 * 2^3 + 1 * 2^2 + 1 * 2^1 + 0 * 2^0 = 22
        decimal += int(binary[i]) * 2 ** ((len(binary) - 1) - i)
    return decimal


# part 2
def calculate_oxygen_rating(arr):
    for i in range(0, len(arr[0])):
        # count zeros and ones
        zeros = 0
        ones = 0
        for element in arr:
            if element[i] == "0":
                zeros += 1
            elif element[i] == "1":
                ones += 1

        # filter array by the most common bit
        if zeros > ones:
            arr = filter_by_bit(arr, "0", i)
        else:
            arr = filter_by_bit(arr, "1", i)

        # if the array has only one element, stop, we got the number
        if len(arr) == 1:
            break

    return arr[0]


def calculate_co2_rating(arr):
    for i in range(0, len(arr[0])):
        # count zeros and ones
        zeros = 0
        ones = 0
        for element in arr:
            if len(arr) == 1:
                break
            if element[i] == "0":
                zeros += 1
            elif element[i] == "1":
                ones += 1

        # filter array by the least common bit
        if zeros <= ones:
            arr = filter_by_bit(arr, "0", i)
        else:
            arr = filter_by_bit(arr, "1", i)

        # if the array has only one element, stop, we got the number
        if len(arr) == 1:
            break

    return arr[0]


def filter_by_bit(arr, bit, digit):
    result = []
    for element in arr:
        if element[digit] == bit:
            result.append(element)
    return result


def calculate_support_rating(arr):
    return binary_to_decimal(calculate_oxygen_rating(arr)) * binary_to_decimal(
        calculate_co2_rating(arr)
    )


# setup
file = open("input.txt", "r")
# list of strings
arr = file.read().split("\n")
file.close()

print(calculate_power_consumption(arr))
print(calculate_support_rating(arr))
