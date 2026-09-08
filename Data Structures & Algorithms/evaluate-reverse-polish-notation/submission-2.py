class Solution:
    def evalRPN(self, x: List[str]) -> int:
        stk=[]
        for token in x:
            if token in {"+", "-", "*","/"}:
                b=stk.pop()
                a=stk.pop()
                if token == "-":
                    res=a-b
                elif token == "+":
                    res=a+b
                elif token == "*":
                    res=a*b
                else: 
                    res=int(a/b)
                stk.append(res)
            else:    
                stk.append(int(token))
        return stk[0]

# tksLst[str]int, stk,4tkintks, 
# from typing import List

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stk = []
        
#         for token in tokens:
#             # 1. Correct way to check for operators
#             if token in {"+", "-", "*", "/"}:
#                 b = stk.pop()
#                 a = stk.pop()
#                 if token == "+":
#                     res = a + b
#                 elif token == "-":
#                     res = a - b
#                 elif token == "*":
#                     res = a * b
#                 else: 
#                     # Python's int() truncation handles the "towards zero" requirement for negative division
#                     res = int(a / b)
                
#                 # 2. Append happens for ALL operators, outside the if/else chain
#                 stk.append(res)
#             else:    
#                 stk.append(int(token))
                
#         return stk[0]