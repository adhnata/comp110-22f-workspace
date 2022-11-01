"""EX04 - Lists - Implement Algorithms to practice computational thinking."""

__author__ = "730616599"


def all(any_length: list[int], one_length: int) -> bool:
    """This function should compare each value in the list to the given integer and see if they all match to provide a true or false statement."""
    i: int = 0
    bool_check: bool = True
    if any_length == 0:
        return False

    while len(any_length) > i and bool_check == True:
        if any_length[i] == one_length:
            i = i + 1
        else:
            bool_check = False
    
    if bool_check ==  False:
        return False
    else:
        return True
    
    
def max(any_length2: list[int]) -> int:
    """This function has the purpose of finding the largest value within the given set."""
    
    if len(any_length2) == 0:
        raise ValueError("max() arg is an empty List")
    
    x: int = 0
    y: int = 1
    z: int = 0
    while len(any_length2) > y:        
        if any_length2[y] > any_length2[x]:
            z = any_length2[y]
            x = x + 1
            y = y + 1
        else:
            z = any_length2[x]
            x = x
            y = y + 1
    return z
    
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Check to see if every value in each list is true."""
    i: int = 0
    
    if len(list_one) != len(list_two):
        return False
    
    while len(list_one) > i:
        if list_one[i] == list_two[i]:
            i = i + 1
        else:
            return False
    
    return True