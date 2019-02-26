import sys

def ascending(a, b):
    return b - a

def descending(a, b):
    return a - b

def selectionSort(xs, compare = ascending):
    remain = xs
    result = []

    while remain:
        selected = reduce(lambda x, y: x if compare(x, y) > 0 else y, remain)
        result += [selected]
        remain = [elt for elt in remain if elt != selected]

    return result

inputNums = [int(input) for input in sys.argv if input.isdigit()]
print "In ascending order:", selectionSort(inputNums)
print "In descending order:", selectionSort(inputNums, descending)
