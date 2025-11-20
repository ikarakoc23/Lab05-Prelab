def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    x = len(s)
    
    _max = 0
    
    res = ""
    
    for i in range(x):
  
        l, r = i, i
        
        while l >= 0 and r < x and s[l] == s[r]:
            
            if (r - l + 1) > _max :
                
                _max = r - l + 1
                
                res = s[l:r+1]
            
            r += 1
            
            l -= 1
     
        l, r = i, i + 1
       
        while l >= 0 and r < x and s[l] == s[r]:
            if (r - l + 1) > _max :
                _max = r - l + 1
                
                res = s[l:r+1]
            
            r += 1
            
            l -= 1

    if _max < 2 :
        return ""  

    return res