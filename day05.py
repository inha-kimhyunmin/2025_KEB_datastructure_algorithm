def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left_half, right_half):
    sorted_list = []

    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1

    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[j:])
    return sorted_list

arr = [7, 9, 103, 30, 102, 35, 2589, 32]
sorted_arr = merge_sort(arr)

print(sorted_arr)

