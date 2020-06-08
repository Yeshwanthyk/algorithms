"""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2

Constraints:

    [time limit] 5000ms

    [input] array.integer arr1
        1 ≤ arr1.length ≤ 100

    [input] array.integer arr2
        1 ≤ arr2.length ≤ 100

    [output] array.integer


"""


"""
Case 1. M ≈ N

arr1 = [1, 2, 3, 5, 6, 7]


arr2 = [3, 6, 7, 8, 20]

Time: O(N + M)

Case 2. M ≫ N
100,000,000 100



arr1 = [1, 2, 3, 5, 6, 7]
                  

arr2 = [3, 6, 7, 8, 20]

Binary search: O(N log M)



When M ≫ N

O(N log M) is better than O(N + M)

Why?

M is much larger than N -> M = N^C


O(N log M) = O(N log N^C) = O( N * C log N) = O(N log N)


O(N + M) = O(N + N^C) = O(N^C)


"""


def find_duplicates(arr1, arr2):

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    dups = []

    if len_arr1 > len_arr2:
        arr1, arr2 = arr2, arr1
        run_binary_search(arr1, arr2)

        return dups


def run_binary_search(arr1, arr2):

    dups = []

    for i in arr1:
        if binary_search(arr2, i):
            dups.append(i)
    return dups


def binary_search(arr, target):

    lo = 0
    hi = len(arr) - 1

    while lo <= hi:

        mid = (lo+hi)//2

        if arr[mid] == target:
            return True

        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


arr1 = [1, 2, 3, 5, 6, 7]


arr2 = [3, 6, 7, 8, 20]

ans = find_duplicates(arr1, arr2)
print(ans)
