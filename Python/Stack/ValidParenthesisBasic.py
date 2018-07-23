# Check for Valid parenthesis using Stacks 

def parCheck(symbolString): 
    s = Stack() 
    
    for string in symbolString: 
        if string == '(':
            s.push(string)
        else: 
            if s.isEmpty(): 
                return False
            else: 
                s.pop() 
    
    if not s.isEmpty():
        return False
    
    return True 


print(parCheck('()()()'))
print(parCheck('((())(()))()'))
print(parCheck(')()('))
print(parCheck('())(()'))