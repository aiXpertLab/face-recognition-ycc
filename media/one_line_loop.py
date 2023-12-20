mylist = [200, 300, 400, 500]

#一般的循环
result = [] 
for x in mylist: 
    if x > 250: 
        result.append(x) 
print(result) # [300, 400, 500]

result = [x for x in mylist if x > 250] 
print(result) # [300, 400, 500]
