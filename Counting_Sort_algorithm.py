def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    range_of_values = max_val - min_val + 1
    count = [0] * range_of_values

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_of_values):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return sorted_arr

if __name__ == "__main__":
    input_array = [4, 2, 2, 8, 3, 3, 1]
    sorted_array = counting_sort(input_array)
    print("Input Array:", input_array)
    print("Sorted Array:", sorted_array)
