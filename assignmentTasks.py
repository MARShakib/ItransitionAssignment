### Task1
import functools


def max_multiplication(text):
    # if not a string return 'nil'
    if not isinstance(text, str):
        return "nil"

    result = 0

    for i in range(len(text) - 3):
        # get subset of four chars in a row
        subText = text[i : i + 4]
        # check all of them are numeric??
        if all(j.isnumeric() for j in subText):
            tempResult = functools.reduce(lambda x, y: int(x) * int(y), subText)
            result = max(tempResult, result)
    return result if result > 0 else "nil"


## Test Cases for Task1
print(max_multiplication("abc12345def"))
print(max_multiplication("abc12345de163452f"))
print(max_multiplication("a1b2c3d4e"))


### Task2
def mySort(Arr):
    # First key for sorting is 1's count in binary and then it's decimal value
    result = sorted(Arr, key=lambda x: (bin(x).count("1"), x))
    return result


## Test Cases for Task2
print(mySort([3, 7, 8, 9]))
print(mySort([9, 7, 8, 3, 10, 11, 5, 16]))
