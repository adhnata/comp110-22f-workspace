"""This is where the function skeletons and implementations will be implemented."""

__author__ = "730616599"

def only_evens(rand_numbs: list[int]) -> list[int]:
    """This function will check a list to see its indexes are even or odd and then return a list of only the even indexes."""
    i: int = 0
    new_list: list[int]
    new_list = []
    
    
    while i < len(rand_numbs):
        if rand_numbs[i] % 2 == 0:
            new_list.append(rand_numbs[i])
            i = i + 1
        else:
             i = i + 1
    
    return new_list
             
def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """This function should take the indexes of two lists and add them together."""
    new_list_two: list[int]
    new_list_two = []
    x: int = 0
    y: int = 0
    while x < len(list_one):
        new_list_two.append(list_one[x])
        x = x + 1
        
    while y < len(list_two):
        new_list_two.append(list_two[y])
        y = y + 1
    
    return new_list_two
    
def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """This function should take the initial list and produce a new list with the values in between the given indexes."""
    new_list_three: list[int]
    new_list_three = []
    if start_index < 0:
        start_index = 0  
        
    if end_index > len(a_list):
        end_index = len(list) - 1
    
    if start_index > len(a_list) or len(a_list) == 0 or end_index == 0 or start_index == end_index:
        return new_list_three == []
    i: int = 0
    

    while i < end_index - start_index + 1:
        if i < start_index:
            i = start_index
        new_list_three.append(a_list[i])
        i = i + 1
    
    return new_list_three
    
    
    
    
            
            
    
            
        
        
        
        