class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                   stack.append(a+b)
                    
                elif i=="*":
                    stack.append(a*b)
                    
                elif i=="-":
                    stack.append(a-b)
                   
                else:
                    ans=int(a/b)
                    stack.append(ans)
            
        return stack.pop()

                    