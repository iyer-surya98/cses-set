def natural_number_sum(number: int) -> int:
    return (number * (number + 1))/2 

def check_split_existence(number: int) -> bool:
    if natural_number_sum(number) % 2 == 0:
        return True
    return False

def split_into_two_sets(number: int) -> tuple[str, tuple[set, set]]:
    """
        https://cses.fi/problemset/task/1092
    """
    if not check_split_existence(number):
        return "NO", (set(),set())
    
    target = int(natural_number_sum(number) / 2)
    set1 = set()
    while target > number:
        set1.add(number)
        target = target - number
        number = number - 1
    set1.add(target)
    return "YES", (set1, set(range(1, number + 1)) - set1)


if __name__ == "__main__":
    print(split_into_two_sets(7))