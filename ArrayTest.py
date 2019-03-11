import time

array1D = [1,2,3,4,5,6,7,8,9]
print ('array1D: ', array1D)
print ('*array1D with sep = \', \'', end=': ')
print (*array1D, sep = ', ', end = '\n\n')

array2D = [[1,2,3],[4,5,6],[7,8,9]]
print ('array2D: ', array2D)
print ('*array2D with sep = \', \'', end=': ')
print (*array2D, sep = ', ', end = '\n\n')

addTest = []
appendTest = []
extendTest = []
for array in array2D:
    addTest += array
    extendTest.extend(array)
    appendTest.append(array)

print ('add : ', addTest)
print ('extend : ', extendTest)
print ('append : ', appendTest, end = '\n\n')

testEltCount = 400000
addTest = []
perfStart = time.perf_counter()
for elt in range(1, testEltCount):
    addTest += [elt]
perfEnd = time.perf_counter()
print ('perf_counter (add %d elts): %.8f' % (testEltCount, perfEnd - perfStart))

extendTest = []
perfStart = time.perf_counter()
for elt in range(1, testEltCount):
    addTest.extend([elt])
perfEnd = time.perf_counter()
print ('perf_counter (extend %d elts): %.8f' % (testEltCount, perfEnd - perfStart))
