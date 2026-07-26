class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        for ch in tokens:
            if ch=='+':
                val=int(self.stack[-1]+self.stack[-2])
                self.stack.pop()
                self.stack.pop()
                self.stack.append(val)
            elif ch=='-':
                val= int(self.stack[-2]-self.stack[-1])
                self.stack.pop()
                self.stack.pop()
                self.stack.append(val)
            elif ch=='*':
                val=int(self.stack[-1]*self.stack[-2])
                self.stack.pop()
                self.stack.pop()
                self.stack.append(val)
            elif ch=='/':
                val= int(self.stack[-2]/self.stack[-1])
                self.stack.pop()
                self.stack.pop()
                self.stack.append(val)
            else :
                val=int(ch)
                self.stack.append(val)
        return val
