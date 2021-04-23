def recursive_function(number: int) -> int:
    if number == 0:
        return 0
    else:
        return number + recursive_function(number - 1)


def visualized_recursive_function(number: int) -> int:
    if number == 0:
        print(number)
        return 0
    else:
        print(number)
        return number + visualized_recursive_function(number - 1)


def compute_summary(number: int) -> int:
    return compute_summary(number)
