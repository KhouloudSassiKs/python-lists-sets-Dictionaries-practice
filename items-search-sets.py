def solution(list1, list2):
    """
    Check whether each element in list1 exists in list2.

    Args:
        list1 (list): A list of elements to check.
        list2 (list): A list of elements to compare against.

    Returns:
        list: A list of booleans, where each value corresponds to
              whether the element in list1 is present in list2.
    """
    set2 = set(list2)
    return [item in set2 for item in list1]


if __name__ == "__main__":
    # Example runs
    print(solution([1, 2, 3], [2, 3, 4]))  
    # [False, True, True]

    print(solution(["apple", "banana", "cherry"], ["banana", "kiwi"]))  
    # [False, True, False]

    print(solution([], [1, 2, 3]))  
    # []

    print(solution([1, 2, 2, 3], [2]))  
    # [False, True, True, False]
