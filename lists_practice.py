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
