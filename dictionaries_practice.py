""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Finds and returns the first number in the list that occurs more than one-third
    of the total number of elements.

    Parameters:
        numbers (List[int]): A list of integers

    Returns:
        int: The first number that appears more than len(numbers) // 3 times.
             Returns -1 if no such number exists.

    Examples:
        findFirstThresholdOcc([3, 1, 3, 3, 2, 1]) >>>>> 3

        findFirstThresholdOcc([1, 2, 3, 4]) >>>>> -1
    """
def findFirstThresholdOcc(numbers):
    occurenceCount = {}
    for number in numbers:
        occurenceCount[number] = occurenceCount.get(number, 0) + 1
        if occurenceCount[number] > len(numbers) // 3:
            return number
    return -1

 """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Counts occurrences of each lego type per box.

    Parameters:
        boxes (List[str]): List of strings, each representing legos in a box.

    Returns:
        Dict[str, Dict[int, int]]: Dictionary where keys are lego names,
        and values are dictionaries mapping box indices to counts.
    """
def legosOccurence(boxes):
    occurenceDictionary = {}
    for index, box in enumerate(boxes):
        legoOccurence = {}
        for lego in box.split():
            legoOccurence[lego] = legoOccurence.get(lego, 0) + 1
        for lego, count in legoOccurence.items():
            if lego in occurenceDictionary:
                occurenceDictionary[lego][index] = count
            else:
                occurenceDictionary[lego] = {index: count}
    return occurenceDictionary
