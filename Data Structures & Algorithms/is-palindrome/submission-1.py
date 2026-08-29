class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)
        for i in range(len(l)):
            if(l[i]!=l[len(l)-i-1]):
                return False
        return True
