import time

from operations import example1, example2, example3


def is_palindrome(s: str) -> bool:
    pure_s = s.replace(" ", "")
    return pure_s == pure_s[::-1]


def polynomial_hash(s: str, p=31, m=(2 ** 31) - 1):
    hash_value = 0
    p_power = 1
    for char in s:
        hash_value = (hash_value + ord(char) * p_power) % m
        p_power = (p_power * p) % m
    return hash_value


def process_operations_with_hash(operations):
    string_hashes = {}
    palindromes = {}
    start_time = time.perf_counter()

    for i in range(10 ** 6):
        operation = operations[i]
        op, string = operation[0], operation[1:].strip()
        string_hash = polynomial_hash(string)

        if op == '+':
            string_hashes[string_hash] = string
            if is_palindrome(string):
                palindromes[string_hash] = string

        elif op == '-':
            if string_hash in string_hashes:
                del string_hashes[string_hash]
                if string_hash in palindromes:
                    del palindromes[string_hash]

        elif op == '?':
            print("yes" if string_hash in string_hashes else "no")

        elif op == '#':
            break
    end_time = time.perf_counter()
    print("Computation time: ", end_time - start_time)

    return palindromes


def test_standard():
    print("Testing standard case")
    return process_operations_with_hash(example1)


def test_10_to_6_length():
    print("Testing case: input length = 10^6 elements")
    return process_operations_with_hash(example2)


def test_excess_length():
    print("Testing case: input length > 10^6 elements")
    return process_operations_with_hash(example3)


def print_all_palindromes(palindromes):
    if palindromes:
        print("Palindromes found:")
        for palindrome in sorted(palindromes.values()):
            print(palindrome)
    else:
        print("No palindromes found.")


if __name__ == "__main__":
    palindromes = test_10_to_6_length()
    print_all_palindromes(palindromes)
