
class TestClass:
    def __init__(self):
        self.hoge = 'hoge'
        self.fuga = 'fuga'

    def provide_hoge(self):
        return self.hoge


test = TestClass()
print(test.hoge)
print(test.provide_hoge())
