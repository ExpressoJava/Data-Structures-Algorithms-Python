"""
Binary Search - the idea is to keep comparing the element with the middle value.  this way
with each search we eliminate one half of the list

Alogrithm:
1. Keep track of two poinster First and Last, These are incremented or decremented to limit
    the part of the list to be searched.

2. Find the middle element of the list: mid = (length of the list) / 2

3. Compare the middle element with the value to be found

4. check if the middle element is lesser than the value to be found
  a. if yes, the element must lie on the second half of the list
  b. if no, the element must lie on the the first half of the list

5. repeat steps 1-3 until the element is found or the end of the list is reached
"""

# Implementation of recursive binary search


# def binary_search(alist, item):
#     if not alist:  # lis is empty -- our base case
#         return False

#     midpoint = len(alist) // 2
#     if alist[midpoint] == item:  # found it!
#         return True

#     if item < alist[midpoint]:  # item is in the first half of list, if at all
#         return binary_search(alist[:midpoint], item)

#     # otherwise item is in the second half of list, if at all
#     return binary_search(alist[midpoint + 1:], item)


# testlist = [2, 3, 5, 9, 11, 15, 17, 19, 33, 39, 55, 76, 99, 101, 117, 220]
# print(binary_search(testlist, 117))  # True
# print(binary_search(testlist, 300))  # False

# Given list B = [2, 5, 7, 8, 9, 11, 15, 17], find if 3 is present in the list or not
# This is iterative binary search
def binary_search(ls, data):
    first = 0
    last = len(ls) - 1
    done = False

    while first <= last and not done:
        mid = (first + last) // 2  # we use // to get whole number
        if ls[mid] == data:
            done = True
        else:
            if ls[mid] > data:
                last = last - 1
            else:
                first = first + 1
    return done


print(binary_search([2, 5, 7, 8, 9, 11, 15, 17], 3))  # False
