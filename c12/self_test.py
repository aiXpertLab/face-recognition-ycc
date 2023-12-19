class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 创建一个Person对象
person = Person("Alice", 25)
# 调用对象的方法
person.say_hello()  # 输出：Hello, my name is Alice and I am 25 years old.