class Bucket:
    def __init__(self, maximum=10 ** 5) -> None:
        self.maximum = maximum
        self.bucket = [0] * maximum

    def append(self, value: int) -> None:
        self.bucket[value] += 1

    def sort(self) -> list:
        cum = []

        for i in range(self.maximum):
            if i == 0:
                cum.append(self.bucket[0])
            else:
                cum.append(self.bucket[i] + cum[i-1])

        result = []

        for i in range(self.maximum):
            result.append()


bucket = Bucket()
print(bucket.bucket)
