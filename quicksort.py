def adoption_count(item):
    return item[1] if isinstance(item, (tuple, list)) else item


def partition(arr, low, high):
    pivot = adoption_count(arr[(low + high) // 2])

    left = low
    current = low
    right = high

    # Place larger counts before the pivot and smaller counts after it.
    while current <= right:
        count = adoption_count(arr[current])

        if count > pivot:
            arr[left], arr[current] = arr[current], arr[left]
            left += 1
            current += 1

        elif count < pivot:
            arr[current], arr[right] = arr[right], arr[current]
            right -= 1

        else:
            current += 1

    return left, right


def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    while low < high:
        left, right = partition(arr, low, high)

        # Recurse on the smaller partition to limit stack usage.
        if left - low < high - right:
            quicksort(arr, low, left - 1)
            low = right + 1
        else:
            quicksort(arr, right + 1, high)
            high = left - 1

    return arr


quick_sort = quicksort


if __name__ == "__main__":
    from pathlib import Path
    from mergesort import count_adoptions, merge_sort

    csv_path = next(
        Path(__file__).parent.glob("Austin_Animal_Center_Outcomes*.csv")
    )

    data = list(count_adoptions(csv_path).items())

    quick_result = quicksort(data.copy())
    merge_result = merge_sort(data.copy())

    assert (
        [row[1] for row in quick_result]
        == [row[1] for row in merge_result]
    ), "Sorting results do not match!"

    print("PASS: Quick Sort matches Merge Sort")
    print("Number of breeds:", len(data))
    print("Top 10 breeds:", quick_result[:10])
