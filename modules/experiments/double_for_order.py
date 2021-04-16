import time


def double_for_order():

    N = 10 ** 4
    over = False

    start = time.time()

    for _ in range(N):
        for __ in range(N):
            current = time.time()
            past_time = current - start
            if past_time > 2:
                print(f"over time ({past_time}s)")
                over = True
                break
        if over:
            break

    if over == False:
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    double_for_order()
