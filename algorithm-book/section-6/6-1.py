import bisect

a = [12, 43, 7, 15, 9]
_a = sorted(a)

for ai in a:
    index = bisect.bisect_left(_a, ai)
    print(ai, index)
