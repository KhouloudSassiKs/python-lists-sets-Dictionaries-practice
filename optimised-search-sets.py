def solution(s, letters):
    """
    Return the sorted list of common characters between two inputs.

    Args:
        s (str): A string of characters.
        letters (iterable): A string or list of characters to compare.

    Returns:
        list: Sorted list of characters found in both `s` and `letters`.
    """
    # Convert both inputs to sets 
    set1 = set(s)
    set2 = set(letters)

    # Find the intersection (common elements)
    common = set1 & set2

    # Return as a sorted list
    return sorted(common)
