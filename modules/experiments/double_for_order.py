import time


def double_for_order():

    N = 10 ** 4

    start = time.time()

    for n in range(N):
        for _n in range(N):
            n * _n

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    double_for_order()
