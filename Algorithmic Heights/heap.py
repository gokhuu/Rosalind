def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def build_heap(arr, n):
    start = n // 2 - 1

    for i in range(start, -1, -1):
        heapify(arr, n, i)


def print_heap(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
        print()


arr = [1, 3, 5, 7, 2]
n = len(arr)
build_heap(arr, n)
print_heap(arr, n)
