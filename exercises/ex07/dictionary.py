"""Dictionary program for EX07 where the function skeletons and implementations will be implemented."""

__author__ = "730616599"

def invert(def_list: dict[str, str]) -> dict[str, str]:
    """Swap each the keys and values of the dictionary."""
    new_dict: dict[str, str]
    new_dict = dict()
    val: str = ""
    
    if def_list == {}:
        return new_dict
    

    for i in def_list:
       val = def_list[i]
       if val not in new_dict:
        new_dict[val] = i
       else: 
        raise KeyError("There are at least two initial inputs with the same value.")
    
    return new_dict

def favorite_color(name_and_color: dict[str, str]) -> str:
    "Find the most popular color."
    new_list: list[str]
    new_list = []
    favorite: str = ""
    favorite_two: str = ""
    
    if name_and_color == {}:
        return favorite_two
    
    for i in name_and_color:
        favorite = name_and_color[i]
        if favorite not in new_list:
            new_list.append(favorite)
        else:
            new_list.append(favorite)
            favorite_two = favorite
    
    return favorite_two
                   
def count(input_list: list[str]) -> dict[str, int]:
    """Takes a list and counts the repeitions to produce a dicitonary."""
    new_dictionary: dict[str, int]
    new_dictionary = dict()
    new_val: str = ""
    
    if input_list == []:
        return new_dictionary
    
    i: int = 0
    while len(input_list) > i:
        new_val = input_list[i]
        if new_val not in new_dictionary:
            new_dictionary[new_val] = 1
        else:
            new_dictionary[new_val] += 1
        
        i += 1
    
    
    return new_dictionary
