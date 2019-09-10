


unsorted = [8,6,5,3,2,1, 10, 11, 43, 56, 67, 87]



'''
8
6
is 8 > 6 ?
yes swap them
'''
def sorted(unsorted):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)):
            if unsorted[i] < unsorted[j]:
                temp = unsorted[i]
                unsorted[i] = unsorted[j]
                unsorted[j] = temp
    return unsorted
print(sorted(unsorted))
