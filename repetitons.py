# https://cses.fi/problemset/task/1069

def length_longest_repetition(dna_string: str) -> int:
    if not dna_string:
        return 0
    max_block_length = 1
    current_block_length = 1
    for i in range(1, len(dna_string)):
        if dna_string[i] == dna_string[i - 1]:
            current_block_length += 1
        else:
            max_block_length = max(max_block_length, current_block_length)
            current_block_length = 1
    max_block_length = max(max_block_length, current_block_length)
    return max_block_length

if __name__ == "__main__":
    print(length_longest_repetition("aaaaaaaccgg"))