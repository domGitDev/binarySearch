

def binary_search(items, value):
    """ binary search requires input
    array to be sorted in ascendent order
    """
    start = 0
    end = len(items)-1

    while(start <= end):
        mid = (start + end)/2
        if items[mid] == value:
            return mid
        elif items[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return -1

