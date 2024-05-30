# longest increasing subsequence

def lengthOfLongestSubstring(s: str) -> int:
    
    charSet = set() # reason we use set here is because it has constant time operation for removal
    l = 0
    maxLen = 0
    for r in range(len(s)):
        if s[r] in charSet: # ----> this is constant time operation, set implements hash internally
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        maxLen = max(maxLen, len(charSet))
    print(maxLen)

lengthOfLongestSubstring("abcdabcbbe")
# Input
# abb 
# "abcabcbb"
 
         


          