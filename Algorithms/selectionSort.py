"""
Selection Sort:
Is about picking/selecting the smallest element from the list and placing it in the
sorted portion of the list. Initially, the first element is considered the minimum
and compared with other elements. During these comparisions, if a smaller element
is found then that is considered the new minimum. After completion of one full round,
the smallest element found is swapped with the first element. this process continues
till all the elements are sorted. 




Algorithm:
1. consider the first element to be sorted and the rest to be unsorted

2. Assume the first element to be the smallest element

3. Check if the first element is the smaller than each of the other elements:
    1. if yes, do nothing
    2. if no, choose the other smaller element as min and repeat step 3.

4. After completion of one iteration through the list, swap the smallest element with the first element 
    of the list

5. Now consider the second element in the list to be the smallest and so on till all elements
    in the list are covered. 


"""


# def selectionSort(alist):

#     for i in range(len(alist)):

#         # Find the minimum element in the remaining
#         minPosition = i
#         for j in range(i+1, len(alist)):
#             if alist[minPosition] > alist[j]:
#                 minPosition = j

#         # Swap the found minimum element with minPosition
#         temp = alist[i]
#         alist[i] = alist[minPosition]
#         alist[minPosition] = temp

#     return alist


# print(selectionSort([5, 2, 1, 9, 0, 4, 6]))  # 0, 1, 2, 4, 5, 6, 9

# Another implementation
array = [1, 45, 10, 35, 100, 13, 147, 600, 80]


def selectionSort(array):

    size = len(array)

    for i in range(0, size):
        for j in range(i+1, size):
            if array[j] < array[i]:
                min = array[j]
                array[j] = array[i]
                array[i] = min


print(array)  # 1, 10, 13, 35, 45, 80, 100, 147, 600
