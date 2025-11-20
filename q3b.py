def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
   
    if a.startswith('0b'):
        
        a = a[2:]
    
    if b.startswith('0b'):
        
        b = b[2:]

    a, b = fill_zeros(a, b)
    
    n = 0
    res = ''
    for i in range(len(a)-1, -1, -1):
        
        bit_sum = (int(a[i])) + (int(b[i])) + n
        
        res = str(bit_sum % 2) + res
        
        n = bit_sum // 2
    
    if n :
        res = '1' + res
    

    i = 0
    
    while i < len(res) and res[i] == '0' :
        
        i += 1
    
    res = res[i:]
    
    if not res :
        
        res = '0'
    
    return '0b' + res

def fill_zeros(a, b):
   
    max_len = max(len(a), len(b))

    a = ('0' * (max_len - len(a))) + a
    
    b = ('0' * (max_len - len(b))) + b
    
    return a, b