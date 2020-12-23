def partition(lst, left = None , right = None):
    if left == None: left = 1
    if right == None: right = len(lst)-1
    pivot = lst[left]
    left_ind = left + 1
    right_ind = right
    while left_ind <= right_ind:
        while left_ind <= right_ind and lst[left_ind] <= pivot:
            left_ind += 1
        while right_ind >= left_ind and lst[right_ind] >= pivot:
            right_ind -= 1
        if left_ind < right_ind:
            lst[left_ind], lst[right_ind] = lst[right_ind], lst[left_ind]
    lst[left], lst[right_ind]= lst[right_ind], lst[left]
    return right_ind



def quick_sort(lst, left=None, right=None):
    if left == None: left = 0
    if right == None: right = len(lst)-1

    # base case
    if left >= right:
        return
    # recursive case
    # p: location(index) of pivot value
    p = partition(lst, left, right)
    quick_sort(lst, left, p - 1)
    quick_sort(lst, p + 1, right)

a = [1, 4, 2, 7, 0]
quick_sort(a)
print(a)