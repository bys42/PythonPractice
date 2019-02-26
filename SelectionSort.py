import sys

def ascending(): return min
def descending(): return max

def selectionSort(list, select = ascending()):
    remain = list.copy()
    result = []

    while remain:
        selection = select(remain)
        result.append(selection)
        remain.remove(selection)

    return result

nums = [int(data) for data in sys.argv if data.isdigit()]
print ("In ascending order:", selectionSort(nums))
print ("In descending order:", selectionSort(nums, descending()))
