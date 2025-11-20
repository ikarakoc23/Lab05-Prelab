def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while non_adjacent_duplicates_exists(s):
        
        res = ""
        
        for i in range(len(s)):
            
            if i < len(s)-1 and s[i] == s[i+1]:
                
                res += s[i+2:]
                
                break
            else :
                res += s[i]
        s = res
    
    return s

def non_adjacent_duplicates_exists(s):
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    
    return False