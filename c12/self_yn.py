class Staff:  # Staff为员工的意思
    bonus = 30000  # bonus为津贴、奖金的意思

    def salary(self):  # salary为工资的意思
        salary = 10000+self.bonus
        return salary

zhang_san = Staff()
zhang_san.bonus = 333
zhang_san_salray = zhang_san.salary()

print(zhang_san_salray)
print(zhang_san.bonus)
