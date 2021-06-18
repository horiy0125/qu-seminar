class Cell:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def get_cell(self, index: int) -> any:
        # O(N)
        tmp_cell = self.head

        for count in range(index+1):
            if count == index:
                return tmp_cell.value

            tmp_cell = tmp_cell.next

    def insert_head(self, value: any) -> None:
        # O(1)
        new = Cell(value)
        self.size += 1

        # 1つ目の要素を追加した場合
        if self.head == None:
            self.head = new
            self.head.next = new
            self.head.prev = new

        new.next = self.head
        new.prev = self.head.prev
        self.head.prev.next = new
        self.head.prev = new
        self.head = new

    def append(self, value: any) -> None:
        # O(1)
        new = Cell(value)
        self.size += 1

        # 1つ目の要素を追加した場合
        if self.head == None:
            self.head = new
            self.head.next = new
            self.head.prev = new

        self.head.prev.next = new
        new.prev = self.head.prev
        new.next = self.head
        self.head.prev = new

    def delete(self, index: int) -> None:
        # O(N)
        tmp_cell = self.head
        head_cell = self.head

        if self.head == None:
            raise ValueError('delete from empty list')
        if index >= self.size:
            raise IndexError('list index out of range')

        self.size -= 1
        for count in range(index+1):
            if count == index:
                tmp_cell.prev.next = tmp_cell.next
                tmp_cell.next.prev = tmp_cell.prev
                if tmp_cell == head_cell:
                    self.head = head_cell.next

            tmp_cell = tmp_cell.next

    def delete_head(self) -> None:
        # O(1)
        if self.head == None:
            raise ValueError('delete from empty list')

        self.size -= 1

        # 要素が1つしかない場合
        if self.head.next == self.head:
            self.head = None
            return

        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def delete_tail(self) -> None:
        # O(1)
        if self.head == None:
            raise ValueError('delete from empty list')

        self.size -= 1

        # 要素が1つしかない場合
        if self.head.next == self.head:
            self.head = None
            return

        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def print_list(self) -> None:
        # O(N)
        tmp_cell = self.head

        # 要素が1つもなかった場合
        if tmp_cell == None:
            print('[]')
            return

        print('[ ', end='')
        for i in range(self.size):
            if i == self.size - 1:
                print(f"{tmp_cell.value} ]")
            else:
                print(tmp_cell.value, end=' -> ')

            tmp_cell = tmp_cell.next

    def std_list(self) -> list:
        # O(N)
        l = []

        tmp_cell = self.head

        while tmp_cell:
            l.append(tmp_cell.value)
            tmp_cell = tmp_cell.next
            if tmp_cell == self.head:
                break

        return l


l = Doubly_linked_list()
l.print_list()
print()

print('add 1, 2, 3 (int) to the list')
l.append(1)
l.append(2)
l.append(3)
l.print_list()
print()

print('add 0 to head of the list')
l.insert_head(0)
l.print_list()
print()

print('add 4, 5, 6 (int) and hoge (str) to the list')
l.append(4)
l.append(5)
l.append(6)
l.append('hoge')
l.print_list()
print()

print('delete 6 from the list')
l.delete(6)
l.print_list()
print()

print('delete last cell (str hoge) from list')
l.delete_tail()
l.print_list()
print()

print('delete head cell (int 0) from the list')
l.delete_head()
l.print_list()
print()

print('search and get the third cell')
print(l.get_cell(2))
