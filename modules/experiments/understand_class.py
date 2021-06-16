
class TestClass:
    def __init__(self) -> None:
        self.hoge = 'hoge'
        self.fuga = 'fuga'

    def provide_hoge(self) -> str:
        return self.hoge


test = TestClass()
print(test.hoge)
print(test.provide_hoge())
