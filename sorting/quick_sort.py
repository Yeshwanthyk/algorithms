def quick_sort(array):

    if len(array) < 1:
        return array

    pivot = array.pop()

    lesser, greater = [], []

    for i in array:
        if i < pivot:
            lesser.append(i)
        else:
            greater.append(i)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


array = [4, 9, 8, 12, 1]
ans = quick_sort(array)
print(ans)
