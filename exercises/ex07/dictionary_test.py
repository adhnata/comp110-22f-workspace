"""Tests for the dictionary.py file."""

__author__ = "730616599"

from exercises.ex07.dictionary import invert, favorite_color, count

def test_invert_long() -> None:
    def_list: dict[str, str] = {"j": "s", "k":"r", "a": "b"}
    assert invert(def_list) == {"s": "j", "r": "k", "b": "a"}
    

def test_invert_short() -> None:
    def_list: dict[str, str] = {"jack": "jill"}
    assert invert(def_list) == {"jill": "jack"}
    

def test_invert_nothing() -> None:
    def_list: dict[str, str] = {}
    assert invert(def_list) == {}
    
    
def test_favorite_color_long() -> None:
    name_and_color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(name_and_color) == "blue"
    

def test_favorite_color_short() -> None:
    name_and_color: dict[str, str] = {"Marc": "yellow", "Kris": "blue"}
    assert favorite_color(name_and_color) == ""
    
    
def test_favorite_color_none() -> None:
    name_and_color: dict[str, str] = {}
    assert favorite_color(name_and_color) == ""
    
    
def test_count_long() -> None:
    input_list: list[str] = ["yellow", "blue","blue"]
    assert count(input_list) == {'yellow': 1, 'blue': 2}
    
    
def test_count_short() -> None:
    input_list: list[str] = ["yellow", "blue"]
    assert count(input_list) == {'yellow': 1, 'blue': 1}
    
    
def test_count_none() -> None:
    input_list: list[str] = []
    assert count(input_list) == {}