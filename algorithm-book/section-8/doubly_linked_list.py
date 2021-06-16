class Element:
    def __init__(self, x) -> None:
        self.x = x
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self) -> None:
        self.head = None

    def insert_tail(self, x) -> None:
        new = Element(x)

        # 1つ目の要素を追加した場合
        if self.head == None:
            self.head = new
            self.head.next = new
            self.head.prev = new

        self.head.prev.next = new
        new.prev = self.head.prev
        new.next = self.head
        self.head.prev = new

    def show(self) -> None:
        tmp_element = self.head
        while tmp_element:
            print(tmp_element.x, 'prev:', tmp_element.prev.x,
                  'next:', tmp_element.next.x)
            tmp_element = tmp_element.next

            if tmp_element == self.head:
                return


l = Doubly_linked_list()
l.insert_tail(0)
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.show()
