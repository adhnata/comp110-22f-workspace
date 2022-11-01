"""This will be the file that holds test functions."""

__author__ = "730616599"



from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_in_order() -> None:
    rand_numbs: list[int] = [1, 2, 3, 4]
    assert only_evens(rand_numbs) == [2, 4]
    
def test_only_evens_out_of_order() -> None:
    rand_numbs: list[int] = [9, 8, 5, 10]
    assert only_evens(rand_numbs) == [8, 10]
    
def test_only_evens_blank() -> None:
    rand_numbs: list[int] = []
    assert only_evens(rand_numbs) == []
    
def test_concat_one_item_each() -> None:
    list_one: list[int] = [1]
    list_two: list[int] = [2]
    assert concat(list_one, list_two) == [1, 2]
    
def test_concat_multiple_items() -> None:
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]

def test_concat_empty() -> None:
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []
    
def test_sub_short_range() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]
    
def test_sub_long_range() -> None:
    a_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    start_index: int = 1
    end_index: int = 7
    assert sub(a_list, start_index, end_index) == [20, 30, 40, 50, 60, 70]
    
def test_sub_no_range() -> None:
    a_list: list[int] = []
    start_index: int = 0
    end_index: int = 0
    assert sub(a_list, start_index, end_index) == []
