"""
Merge Sort:
Recursive algorithm that continually splits a list in half. If the list is empty or has one item,
it's sorted by definition(the base case). If the list has more than one item, we split the list and
recursively invoke a merge sort on both halves
Once the two halves are sort, merge is performed. Merging two smaller sorted lists
and combining them together into single, sorted, new list. 

Can be used to sort an unsorted list or merge two sorted lists

Algo:
1. split the unsorted list into groups recursively until there is one element per group

2. Compare each of the elements and then group them

3. repeat step 2 until the whole list is merged and sorted into the process


"""


def mergeSort(alist):
    print("splitting ", alist)

    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # Recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1

            else:
                alist[k] = righthalf[j]
                j = j + 1

            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
