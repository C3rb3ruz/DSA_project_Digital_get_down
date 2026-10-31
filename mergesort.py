import csv
import sys

def count_adoptions(path):
    counts = {}
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Outcome Type"] == "Adoption":
                key = row["Breed"]
                counts[key] = counts.get(key, 0) + 1
    return counts

def merge(left, right):
    sorted_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def main():
    counts = count_adoptions("DSA_project_Digital_get_down/Austin_Animal_Center_Outcomes_(10_01_2013_to_05_05_2025)_20261031.csv")
    sorted_arr = merge_sort(list(counts.items()))
    for x in range(10):
        print(sorted_arr[x])
    
if __name__ == "__main__":
    main()