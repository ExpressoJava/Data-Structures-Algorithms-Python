"""
Insertion Sort is a simple sorting algorithm that works the way we sort playing cards
in our hands.

Algorithms:
Sort an arr[] of size n
Insertion sort(arr, n)
Loop from -1 to n-1
Pick an element arr[i] and inserrt it into sorted sequence arr[0...i-1]

Example: 12, 11, 12, 5, 6
Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

When i = 1. 
Since 11 < 12, move 12 and insert 11 before 12.

11, 12, 13, 5, 6

When i = 2. 
13 will remain since all elements in A[0...i-1] < 13

11, 12, 13, 5, 6

When i = 3. 
5 will move to the beginning an all other elements from 11 to 13 will move
one position ahead of their current position.

5, 11, 12, 13, 6

When i = 4.
6 will move to the poistion after 5 and elements from 11 to 13 will move one position
ahead of their current position

5, 6, 11, 12, 13

"""


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0...i-1], that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Testing
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])  # 5, 6, 11, 12, 13
