class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count

# 创建两个Counter对象
counter1 = Counter()
counter2 = Counter()

# 调用对象的方法
counter1.increment()
counter1.increment()
counter2.increment()

# 获取对象的属性
count1 = counter1.get_count()
count2 = counter2.get_count()
print(f"counter1 count: {count1}")  # 输出：counter1 count: 2
print(f"counter2 count: {count2}")  # 输出：counter2 count: 1