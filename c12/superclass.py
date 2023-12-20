class A:
    def work(self):
        print("A.work")

class B(A):
    def work(self):
        print("B (A) ")

    def super_work(self):
        print("b.__bases__")
        self.work()
        super(B, self).work()
        super().work()

b=B()
b.super_work()

