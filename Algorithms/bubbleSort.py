"""
Bubble Sort:
We start at the beginningof unsorted list and compare each element to its right hand 
neigbhor. If the right hand neighbor/element is smaller gets shifted to the left.

The above is repeated ntil we passed through the entire collection/array/list
without performing a single swap/shift. With each pass the larger elements will "bubble"
toward the right hand side of the collection

Conclusion:
We need n-1 passes through the collection for every elemnt to "bubble up"
to its correct position

Worse case runtime complexitiy: O(n2)
"""

# Implementation:


def bubbleSort(alist):

    # Setting the range for comparision (first round: n, 2nd round: n-1 and so on)
    for i in range(len(alist)-1, 0, -1):

        # Comparing within set range
        for j in range(i):

            # Comparing element with its right side neighbor
            if alist[j] > alist[j+1]:

                # Swapping
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

    return alist


print(bubbleSort([10, 15, 9, 7, 5, 1, 55, 90]))
