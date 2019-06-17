def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

    sorted_items = reversed_mergesort(input_list)

    list1 = list()
    list2 = list()

    for item in sorted_items:
        if len(list1) > len(list2):
            list2.append(str(item))
        else:
            list1.append(str(item))

    return [int("".join(list1)), int("".join(list2))]


def reversed_mergesort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = reversed_mergesort(left)
    right = reversed_mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged_items = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_items.append(right[right_idx])
            right_idx += 1
        else:
            merged_items.append(left[left_idx])
            left_idx += 1

    merged_items += left[left_idx:]
    merged_items += right[right_idx:]
    return merged_items


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
