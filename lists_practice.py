 """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Rotates digits among a list of numbers based on position.
    
    At each step:
    - The i-th digit from the right (1-indexed) is removed from each number (if it exists)
    - That digit is inserted at the beginning of the *next* number (cyclically)
    The process repeats for each digit position (from right to left) until no changes occur.

    Parameters:
        numbers (List[int]): A list of integers to rotate digits among

    Returns:
        List[int]: Final list of integers after all digit rotations are complete

    Examples:
        rotate_numbers([123, 234, 345, 456]) >>>> [362, 433, 144, 255]
        rotate_numbers([15, 156, 123]) >>>> [615, 121, 53]
    """
def rotate_numbers(numbers):
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

    return [int(num) for num in rotated]
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
String-based multiplication of large integers.

This module implements a manual multiplication algorithm that works
on arbitrarily large non-negative integers represented as strings.
It mimics the long multiplication process taught in school:

    123
  × 456
  ------
    738   (123 × 6)
   615    (123 × 5, shifted one place)
  492     (123 × 4, shifted two places)
  ------
  56088

Each digit of `num2` is multiplied by all digits of `num1`,
producing partial products, which are then summed using `sumNumbers`.

Functions:
----------
solution(num1: str, num2: str) -> str
    Multiplies two integer strings and returns their product as a string.
    Handles arbitrarily large inputs without relying on Python's built-in
    integer multiplication.

sumNumbers(num1: str, num2: str) -> str
    Adds two integer strings and returns their sum as a string.
"""
def solution(num1, num2): 
    if num1 == "0" or num2 == "0":
        return "0"

    output = [] 
    # iterate right-to-left through num2
    for j in range(len(num2)-1, -1, -1):  
        b = int(num2[j]) 
        carry = 0 
        subOutput = [] 

        # place shifting (j from right means that many zeros at the end)
        subOutput.extend(["0"] * (len(num2) - 1 - j))  

        # inner loop: multiply digit b with all digits of num1
        for i in range(len(num1)-1, -1, -1): 
            a = int(num1[i]) 
            res = a * b + carry 
            carry = res // 10
            subOutput.insert(0, str(res % 10)) 

        if carry > 0: 
            subOutput.insert(0, str(carry)) 

        output.append("".join(subOutput)) 

    # Add all partial results
    finalSum = "0" 
    for item in output: 
        finalSum = sumNumbers(finalSum, item) 
                
    return finalSum.lstrip("0") or "0"


def sumNumbers(num1, num2): 
    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, [] 
    while i >= 0 or j >= 0 or carry > 0: 
        n1 = int(num1[i]) if i >= 0 else 0 
        n2 = int(num2[j]) if j >= 0 else 0 
        total = n1 + n2 + carry 
        carry = total // 10
        res.append(str(total % 10)) 
        i, j = i - 1, j - 1 
    return ''.join(res[::-1])
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    For each starting position i in the board:
    - Jump forward board[i] steps at a time.
    - Count how many moves until exiting the board.
    - If an obstacle is encountered along the way, return -1 for that start.

    Args:
        board (list[int]): Array of jump sizes at each index.
        obstacle (int): Value representing an obstacle in the board.

    Returns:
        list[int]: Moves needed from each index to exit, or -1 if blocked.

    Example:
        navigateBoard([2, 3, 1, 1, 4], obstacle=3) >>>>> [3, -1, 2, 2, 1]

        Execution trace:
        - Start at index 0: jumps → 0→2→3→4→exit → 3 moves
        - Start at index 1: board[1] = 3 (obstacle), so result = -1
        - Start at index 2: jumps → 2→3→4→exit → 2 moves
        - Start at index 3: jumps → 3→4→exit → 2 moves
        - Start at index 4: jumps → 4→exit → 1 move
    """
 def navigateBoard(board, obstacle):
    output = []
    n = len(board)

    for i in range(n):
        moves = 0
        pos = i

        # Immediate obstacle at start
        if board[pos] == obstacle:
            output.append(-1)
            continue

        while pos < n:
            newPos = pos + board[pos]

            if newPos < n and board[newPos] == obstacle:
                # Next jump lands on an obstacle
                moves = -1
                break

            pos = newPos
            moves += 1

        output.append(moves)

    return output
