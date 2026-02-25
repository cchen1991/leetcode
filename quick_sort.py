def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = _partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    import random

    data = [random.randint(-100, 100) for _ in range(20)]
    print("原始数组:", data)
    print("快排结果:", quick_sort(data))

    data2 = data[:]
    quick_sort_in_place(data2)
    print("原地快排:", data2)
