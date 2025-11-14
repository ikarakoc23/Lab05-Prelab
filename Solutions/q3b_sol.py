def add_binary(a, b):
    # Remove the '0b' prefix
    if a.startswith('0b'):
        a = a[2:]
    if b.startswith('0b'):
        b = b[2:]
    # Pad the shorter string with zeros
    a, b = fill_zeros(a, b)
    
    carry = 0
    result = ''
    for i in range(len(a)-1, -1, -1):
        bit_sum = (int(a[i])) + (int(b[i])) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
    if carry:
        result = '1' + result
    
    # Remove leading zeros
    i = 0
    while i < len(result) and result[i] == '0':
        i += 1
    result = result[i:]
    if not result:
        result = '0'
    return '0b' + result

def fill_zeros(a, b):
    maxlen = max(len(a), len(b))
    # Implement zero-filling using string operations
    a = ('0' * (maxlen - len(a))) + a
    b = ('0' * (maxlen - len(b))) + b
    return a, b
