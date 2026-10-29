def partition(arr, low, high):
    pass


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)