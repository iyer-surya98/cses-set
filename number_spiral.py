def calculate_diagonal_value(index: int):
    return index * (index - 1) + 1

def number_spiral_at(row: int, column: int) -> int | str:
    """
       https://cses.fi/problemset/task/1071 
    """
    # the number spiral coordinates start from (1,1)
    if row <= 1 or column <= 1:
        return -1
    
    if row == column:
        # use formula
        return calculate_diagonal_value(row)
    
    nearest_diagonal_index = max(row, column)
    value_at_diagonal = calculate_diagonal_value(nearest_diagonal_index)

    if nearest_diagonal_index % 2 == 0:
        column_diff_sign = 1
        row_diff_sign = -1
    else:
        column_diff_sign = -1
        row_diff_sign = 1
    
    if row - nearest_diagonal_index < 0:
        return value_at_diagonal + row_diff_sign * (nearest_diagonal_index - row)

    return value_at_diagonal + column_diff_sign * (nearest_diagonal_index - column)
    

if __name__ == "__main__":
    print(number_spiral_at(4,2)) 