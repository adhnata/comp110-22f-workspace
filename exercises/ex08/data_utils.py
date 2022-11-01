"""Dictionary related utility functions."""

__author__ = "730616599"

from csv import DictReader

# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str,]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    #Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result
    
    
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
        
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    
    return result
    
    
def head(column_table: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first couple of rows of data for each column."""
    new_dict: dict[str, list[str]] = {}
    
    for first_row in column_table:
        new_list: list[str] = []
        i: int = 0
        while len(column_table[first_row]) > i and row > i:
            new_list.append(column_table[first_row][i])
            i += 1
        new_dict[first_row] = new_list
    
    return new_dict


def select(col_based: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    new_dict: dict[str, list[str]] = {}
    
    for columns in col_names:
        if columns in col_based:
            new_dict[columns] = col_based[columns]
    
    return new_dict


def concat(col_table_one: dict[str, list[str]], col_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column based table by combining two column based tables."""
    new_list: dict[str, list[str]] = {}
    
    for columns in col_table_one:
        new_list[columns] = col_table_one[columns]
        
    for columns in col_table_two:
        if columns not in new_list:
            new_list[columns] = col_table_two[columns]
        else:
            new_list[columns] += col_table_two[columns]
    
    return new_list


def count(value_list: list[str]) -> dict[str, int]:
    """Produce a dictionary with unique keys and values that have been counted if repeated."""
    new_dictionary: dict[str, int] = {}
    new_val: str = ""
    i: int = 0
    while len(value_list) > i:
        new_val = value_list[i]
        if new_val not in new_dictionary:
            new_dictionary[new_val] = 1
        else:
            new_dictionary[new_val] += 1
        
        i += 1
        
    return new_dictionary