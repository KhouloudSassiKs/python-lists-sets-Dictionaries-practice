def solution(s, letters):
    """
    Return the sorted list of common characters between two inputs.

    Args:
        s (str): A string of characters.
        letters (iterable): A string or list of characters to compare.

    Returns:
        list: Sorted list of characters found in both `s` and `letters`.
    """
    # Convert both inputs to sets for fast membership checking
    set1 = set(s)
    set2 = set(letters)

    # Find the intersection (common elements)
    common = set1 & set2

    # Return as a sorted list
    return sorted(common)


if __name__ == "__main__":
    # Example usages
    print("Example 1:", solution("hello", "world"))       # ['l', 'o']
    print("Example 2:", solution("abcdef", "xyz"))        # []
    print("Example 3:", solution("mississippi", "imps"))  # ['i', 'm', 'p', 's']
    print("Example 4:", solution("python", ['p', 'y', 'z']))  # ['p', 'y']
