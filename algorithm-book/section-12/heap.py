class Heap:
    def __init__(self) -> None:
        self.heap = []

    def top(self) -> any:
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            raise IndexError('heap has no value')

    def push(self, value) -> None:
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            p = int((i - 1) / 2)

            if self.heap[p] >= value:
                break

            self.heap[i] = self.heap[p]
            i = p

        self.heap[i] = value


heap = Heap()
heap.push(19)
heap.push(12)
heap.push(15)
heap.push(10)
heap.push(7)
heap.push(6)
heap.push(1)
heap.push(3)
heap.push(7)
heap.push(5)
heap.push(3)
heap.push(2)
print(heap.heap, len(heap.heap))
