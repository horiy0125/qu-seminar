def for_loop(N: int) -> int:
    fibonacci_numbers = [0, 1]

    if N >= 2:
        for n in range(2, N+1):
            fibonacci_number = fibonacci_numbers[n-1] + fibonacci_numbers[n-2]
            fibonacci_numbers.append(fibonacci_number)

    return fibonacci_numbers[N]


print('\n')
print('answer:', for_loop(10 ** 7))
print('\n')
