def smaller(left: list, right: list):
    if left > right:
        return right
    else:
        return left


def search_minimum(array: list):

    if len(array) == 1:
        return array[0]
    else:
        split_index = int(len(array) / 2)

        left = search_minimum(array[:split_index])
        right = search_minimum(array[split_index:])

        return smaller(left, right)


a = [1, 5, 3, 7, 5, 4, 8, 0, -1, -111]
print(search_minimum(a))
