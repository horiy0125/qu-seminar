import time


def for_order():

    N = 10 ** 7
    over = False

    start = time.time()

    for _ in range(N):
        current = time.time()

        past_time = current - start
        if past_time > 2:
            print(f"over time ({past_time}s)")
            break

    end = time.time()

    if over == False:
        print(end - start)


if __name__ == "__main__":
    for_order()
