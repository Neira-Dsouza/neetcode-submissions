class Solution:
    def isValid(self, s: str) -> bool:
        bracket={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or bracket[i]!=stack.pop():
                    return False
        return len(stack)==0             

        