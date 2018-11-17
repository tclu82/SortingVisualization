BUCKET_COUNT = 10

def bucket_sort(array):
    # Corner case
    if len(array) == 0:
        return array
    # Find max and min value
    minValue = min(array)
    maxValue = max(array)
    # Initialize bucket
    buckets = []
    for i in range(0, BUCKET_COUNT):
        buckets.append([])
    # Calculate bucket length
    bucket_length = (maxValue - minValue) // BUCKET_COUNT + 1
    # Assign value into bucket
    for i in range(0, len(array)):
        buckets[(array[i] - minValue) // bucket_length].append(array[i])
    # Output
    result = []
    for i in range(0, len(buckets)):
        buckets[i].sort()
        for j in range(0, len(buckets[i])):
            result.append(buckets[i][j])
    return result

def shell_sort(array):
    def check_gap(gap_length, array, index):
        value = array[index]
        # Check 2 elements with gap length distance to see if need to swap
        while index >= gap_length and array[index-gap_length] > value:
            array[index] = array[index-gap_length]
            index = index-gap_length
        # Put it back
        array[index] = value

    def gap_sort(array, start_index, gap_length):
        for index in range(start_index + gap_length, len(array), gap_length):
            check_gap(gap_length, array, index)

    # Start gap length
    gap_length = len(array) // 2
    # gap length divided by 2
    while gap_length > 0:
        for start_index in range(gap_length):
            gap_sort(array, start_index, gap_length)
        gap_length = gap_length // 2
    return array

nums = input('Enter the list of (nonnegative) numbers: ').split()
nums = [int(x) for x in nums]

sorted_list = bucket_sort(nums)
# sorted_list = shell_sort(nums)

print(sorted_list)
