def weird_algorithm(number: int) -> None:
    """The "weird algorithm" is just `3x + 1`. If x is even, the algorithm divides 
    it by two, and if x is odd, the algorithm multiplies it by three and adds one. 
    The algorithm repeats this, until x is one. 
    
    For example, the sequence for `x` = 3 is as follows:
    3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    Args:
        number (int): The initial integer which starts the process.
    """
    print(number, end = ' ')
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number, end = ' ')
        else:
            number = int(3 * number + 1)
            print(number, end = ' ')

if __name__ == "__main__":
    number = int(input())
    weird_algorithm(number) 