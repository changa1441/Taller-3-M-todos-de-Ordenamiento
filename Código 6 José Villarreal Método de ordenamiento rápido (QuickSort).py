def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)

    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quicksort(arr)
    print(sorted_arr)
