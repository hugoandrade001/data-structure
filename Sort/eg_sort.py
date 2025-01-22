 


def insertion_sort(l: list) -> None:
    for i in range(1, len(l)):
        # Repeatedly shift elements rightward
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        # Place element i
        l[j + 1] = key


"""
Maintains sorted left sub-array, and repeatedly selects the minimum element from the unsorted
sub-array to place at the end of the left sub-array
O(n^2), in-place, not stable
"""
def selection_sort(l: list) -> None:
    for i in range(len(l) - 1):
        # Find minimum element index in remaining sub-array
        min_i = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_i]:
                min_i = j
        # Swap min element with start of unsorted sub-array
        l[i], l[min_i] = l[min_i], l[i]

"""
Merge two sorted lists in O(n) time. Requires O(n) extra space
"""
def merge(a: list, b: list) -> list:
    a_i, b_i, c = 0, 0, []

    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:  # using '<=' here makes mergesort stable
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1

    if a_i < len(a):
        c.extend(a[a_i:])
    elif b_i < len(b):
        c.extend(b[b_i:])

    return c

"""
Recursively sorts left, right sub-arrays and then merges with
linear merge sub-routine
O(n*log(n)), not in-place, stable
"""
def merge_sort(l: list) -> list:
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    return merge(merge_sort(l[:mid]), merge_sort(l[mid:]))


"""
Rearrange arr[lo...hi] in-place in linear time such that all elements
less than pivot are left of it, and all elements greater than or equal to pivot
are right of it.
Return pivot index
lo and hi are inclusive indices within which to partition
"""
def partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[hi]  # arbitrarily choosing last element as pivot
    pivot_idx = hi
    hi -= 1
    # maintain arr[left of lo] < pivot, arr[right of hi] >= pivot
    while lo <= hi:
        if arr[lo] < pivot:
            lo += 1
        else:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            hi -= 1

    arr[lo], arr[pivot_idx] = arr[pivot_idx], arr[lo]
    return lo


"""
Partitions array, then recursively sorts left and right sub-arrays
Expected O(n*log(n)), in-place, not stable
"""
def quick_sort(arr: list, lo=None, hi=None) -> None:
    if lo is None:
        lo, hi = 0, len(arr) - 1
    if hi <= lo:
        return
    pivot_idx = partition(arr, lo, hi)
    quick_sort(arr, lo, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, hi)



def binary_search(arr: list, elt) -> int:
    """
    :param arr: A sorted array
    :param elt: The element to search for
    :return: The index of the target element. -1 if not present
    If target element is present multiple times, returns one of these indices
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == elt:
            return mid
        elif arr[mid] > elt:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1



l = [4, 3, 2, 7, 8, 1, 5, 6]
# insertion_sort(l)
# selection_sort(l)
# print(merge_sort(l))

quick_sort(l)
print(l)

for i in range(10):
    print(binary_search(l, i))