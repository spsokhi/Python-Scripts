
def selectionsort(a):
    for i in range(len(a)-1):
        min = a[i]
        pos = i
        for j in range(i+1, len(a)):
            if a[j] < min:
                min = a[j]
                pos = j
        a[i], a[pos] = min, a[i]


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

selectionsort(a)
print('After sorting elements are: ', a)
