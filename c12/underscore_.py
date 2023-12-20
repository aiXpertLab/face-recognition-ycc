#variable name having single leading underscore.
_a="hello underscore"
b=" no underscore"
 
def add(x,y):
    print (x+y)

#function name having single leading underscore
def _sub(x,y):
    print (x-y)
 
if __name__ == '__main__':
    print (_a)#Output:hello
    print(b)
    add(4,3)#Output:7
    _sub(4,3)#Output:1