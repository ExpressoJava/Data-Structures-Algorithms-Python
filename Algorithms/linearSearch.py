"""
Linear(Sequential) Search - When data items are stored in a collections such as a list, we can say they have a linear/sequential 
relationship.

Example: 
Searching for "Harry Potter" book, from shelf in a poorly lit room how would you go about it?

You can start at one end and take a look at one book at a time & check if it's "Harry Potter" or not. You would
check every book until "Harry Potter" is found or the end of shelf is reached. 

-Best case scenario would be when Harry Potter is the first book
-Worst case sencario would be the book is NOT there

Implementation:
Given list A = [6, 3, 9, 0, 5, 8, 2]

Find if 0 is present in this list or not

pseudo:
1. Take one number at a time from list A

2. compare it w/ 0 & check if it is match
  a. if yes, return True
  b. if no, return False

3. if the end of list, return False

Note: Can be done with both sorted/unsorted items

"""


# def linearSearch(ls, data):
#     for item in ls:
#         if item == data:
#             return True

#     return False


# # print(linearSearch([6, 3, 9, 0, 5, 8, 2], 0)) # True
# print(linearSearch([6, 3, 9, 0, 5, 8, 2], 10))  # False

def sequential_search(alist, item):
    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True
        position += 1  # position = posistion + 1

    return False


testList = [1, 3, 33, 9, 19, 20, 56, 12, 0]

print(sequential_search(testList, 3))  # True
print(sequential_search(testList, 99))  # False
