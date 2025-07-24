# https://cses.fi/problemset/task/1083
def find_missing_number(max_integer, list_of_numbers):
    """
    Takes as input a list of numbers between 1 and length of the list (inclusive)
    and returns the missing number from that range. 
    """
    list_of_numbers = list(map(int, list_of_numbers))
    return sum(
        list(
            range(1, max_integer + 1)
        )
    ) - sum(list_of_numbers)


if __name__ == "__main__":
    max_integer = int(input())
    numbers = str(input())
    print(find_missing_number(max_integer, numbers.split()))