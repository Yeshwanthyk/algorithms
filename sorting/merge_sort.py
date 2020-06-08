def merge_sort(array):

    if len(array) < 1:
        return []

    mid = len(array)//2

    left = array[:mid]
    right = array[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):

    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    return merged + left + right


# array = [4, 9, 8, 12, 1]
array = [[7, 9], [4, 12]]
ans = merge_sort(array)
print(ans)
