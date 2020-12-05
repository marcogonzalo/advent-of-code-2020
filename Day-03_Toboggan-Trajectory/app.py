import input

def tree_counter(arr, stepsToRight = 3, stepsToDown = 1):
    arrlen, strlen = len(arr), len(arr[0])
    counter, right, down = 0, 0, 0
    while down + 1 < arrlen:
        right = right + stepsToRight
        down = down + stepsToDown
        if right + 3 >= strlen: right = right - strlen
        if arr[down][right] == '#': counter = counter + 1

    return counter

product = 1
for slope in input.slopes:
    product = product * tree_counter(input.trees, slope[0],slope[1])

print('Product of tree quantities:', product)
