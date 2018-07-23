# Convert an integer to Binary using stack

def convert2bin(integer): 
    s = Stack()
    
    while integer != 0:
        rem = integer % 2
        s.push(rem)
        integer //=2
    
    res = "" 
    
    while not s.isEmpty():
        res += str(s.pop())
    
    return res

print(convert2bin(233)) # 11101001
print(convert2bin(1)) # 1
print(convert2bin(10)) # 1010
print(convert2bin(4)) # 100

