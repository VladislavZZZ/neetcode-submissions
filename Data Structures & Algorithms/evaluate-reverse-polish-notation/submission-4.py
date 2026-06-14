class Solution:
    operands = ["+","-","*","/"]
    st=[]
    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            if token == "+":
                op2, op1 = self.st.pop(), self.st.pop()
                result = op1+op2
                self.st.append(result)
            elif token == "-":
                op2, op1 = self.st.pop(), self.st.pop()
                result = op1-op2
                self.st.append(result)
            elif token == "*":
                op2, op1 = self.st.pop(), self.st.pop()
                result = op1*op2
                self.st.append(result)
            elif token == "/":
                op2, op1 = self.st.pop(), self.st.pop()
                result = int(op1/op2)
                self.st.append(result)
            else:
                self.st.append(int(token))
        return self.st[-1]