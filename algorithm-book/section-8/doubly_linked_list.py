class Cell:
    def __init__(self, x) -> None:
        self.x = x
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self) -> None:
        self.head = None

    def append(self, x) -> None:
        # O(1)
        new = Cell(x)

        # 1つ目の要素を追加した場合
        if self.head == None:
            self.head = new
            self.head.next = new
            self.head.prev = new

        self.head.prev.next = new
        new.prev = self.head.prev
        new.next = self.head
        self.head.prev = new

    def insert_head(self, x) -> None:
        # O(1)
        new = Cell(x)

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

    def delete(self, x) -> None:
        # Pythonではポインタ渡しができないためO(1)ではなくO(N)
        tmp_cell = self.head
        head_cell = self.head

        if self.head == None:
            raise ValueError('delete from empty list')

        delete_count = 0
        while tmp_cell:
            if tmp_cell.x == x:
                delete_count += 1
                tmp_cell.prev.next = tmp_cell.next
                tmp_cell.next.prev = tmp_cell.prev
                if tmp_cell == self.head:
                    self.head = self.head.next
                return
            tmp_cell = tmp_cell.next
            if tmp_cell == head_cell:
                if delete_count == 0:
                    raise ValueError('value not in list')
                return

    def delete_head(self) -> None:
        # O(1)
        if self.head == None:
            raise ValueError('delete from empty list')

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

        # 要素が1つしかない場合
        if self.head.next == self.head:
            self.head = None
            return

        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def std_list(self) -> list:
        # O(N)
        l = []

        tmp_cell = self.head

        while tmp_cell:
            l.append(tmp_cell.x)
            tmp_cell = tmp_cell.next
            if tmp_cell == self.head:
                break

        return l

    # def show(self) -> None:
    #     tmp_cell = self.head
    #     print('[', end='')

    #     while tmp_cell:
    #         print(f"{tmp_cell.x}", end='')
    #         tmp_cell = tmp_cell.next

    #         if tmp_cell == self.head:
    #             print(']')
    #             return
    #         else:
    #             print(', ', end='')


l = Doubly_linked_list()
print(l.std_list())
print()

print('add 1, 2, 3 (int) to the list')
l.append(1)
l.append(2)
l.append(3)
print(l.std_list())
print()

print('add 0 to head of the list')
l.insert_head(0)
print(l.std_list())
print()

print('add 4, 5, 6 (int) and hoge (str) to the list')
l.append(4)
l.append(5)
l.append(6)
l.append('hoge')
print(l.std_list())
print()

print('delete 6 from the list')
l.delete(6)
print(l.std_list())
print()

print('delete last cell (str hoge) from list')
l.delete_tail()
print(l.std_list())
print()

print('delete head cell (int 0) from the list')
l.delete_head()
print(l.std_list())
