def rotate_numbers(numbers):
    """
    Rotates digits among a list of numbers based on position.

    At each step:
    - The i-th digit from the right (1-indexed) is removed from each number (if it exists)
    - That digit is inserted at the beginning of the *next* number (cyclically)

    The process repeats for each digit position (from right to left) until no changes occur.

    Parameters:
        numbers (List[int]): A list of integers to rotate digits among

    Returns:
        List[int]: Final list of integers after all digit rotations are complete

    Example:
        >>> rotate_numbers([123, 234, 345, 456])
        [362, 433, 144, 255]

        >>> rotate_numbers([15, 156, 123])
        [615, 121, 53]
    """
    rotated = [str(el) for el in numbers]
    max_digits = max(len(item) for item in rotated)
    n = len(numbers)
    index = max_digits - 1

    while True:
        extracted = []
        rotating_digits = []
        previous = rotated.copy()

        for i in range(n):
            num = rotated[i]
            if len(num) <= index:
                extracted.append(num)
                rotating_digits.append('')
            else:
                extracted.append(num[:index] + num[index + 1:])
                rotating_digits.append(num[index])

        for i in range(n):
            rotated[i] = (rotating_digits[i - 1] if i != 0 else rotating_digits[-1]) + extracted[i]

        if rotated == previous:
            break

        index = max_digits - 1 if index == 0 else index - 1
