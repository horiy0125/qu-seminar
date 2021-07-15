class Heap:
    def __init__(self) -> None:
        self.heap = []

    def top(self) -> any:
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return
            # raise IndexError('length of heap is 0')

    def push(self, value) -> None:
        if type(value) != int and type(value) != float:
            raise TypeError('value must be number')

        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            p = int((i - 1) / 2)

            if self.heap[p] >= value:
                break

            self.heap[i] = self.heap[p]
            i = p

        self.heap[i] = value

    def pop(self) -> None:
        if len(self.heap) == 0:
            return

        l = len(self.heap) - 1
        top = self.heap[l]
        self.heap = self.heap[:l]

        i = 0
        while i * 2 + 1 < len(self.heap):
            child1 = i * 2 + 1
            child2 = i * 2 + 2

            if child2 < len(self.heap) and self.heap[child2] > self.heap[child1]:
                child1 = child2

            if self.heap[child1] <= top:
                break

            self.heap[i] = self.heap[child1]
            i = child1

        self.heap[i] = top


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
heap.pop()
print(heap.heap, len(heap.heap))
