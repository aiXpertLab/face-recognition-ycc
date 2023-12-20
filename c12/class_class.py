# 创建一个A类
class A:
    def a(self):
        return print('这里是A类')

class B:
    # 实例化A类达到调用目的
    def run_a(self):
        print("c33:")
        self.a=A()
        self.a.a()
        # 这样就调用到了a类的方法了
# 继承自A类，什么是继承，请自行百度

class C(A):
    pass

print("c:")
c=C() # 实例化C类
# 有了继承自A的方法，所以直接使用A类的方法就好
c.a() #这样也是同样的效果噢