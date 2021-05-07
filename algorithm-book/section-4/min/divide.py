count = 0


def smaller(left: int, right: int):
    if left > right:
        return right
    else:
        return left


def search_minimum(array: list):

    global count
    count += 1

    print(array)

    if len(array) == 1:
        return array[0]
    else:
        split_index = len(array) // 2

        left = search_minimum(array[:split_index])
        right = search_minimum(array[split_index:])

        return smaller(left, right)


a = [1, 5, 3, 7, 5, 4, 8, 0, -1, -111]
# a = [1, 5, 3, 7, 5, 4, 8, 0]
print(search_minimum(a), count)
