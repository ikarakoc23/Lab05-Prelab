def longest_palindromic_substring(s):
    n = len(s)
    max_len = 0
    result = ""
    
    for i in range(n):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                max_len = r - l + 1
                result = s[l:r+1]
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                max_len = r - l + 1
                result = s[l:r+1]
            l -= 1
            r += 1

    if max_len < 2:
        return ""  # If no palindromic substring of length >= 2

    return result