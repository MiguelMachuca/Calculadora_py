#
#
# class decifrar:
#
#     def __int__(self, valor):
#         self.__valor = valor
#
#     def separar_valores(self):
#         self.__valor
#
#
# #Algorithm ConvertInfixtoPrefix
# # Purpose: Convert an infix expression into a prefix expression. \
#
# def operando(valor):
#     if valor == '(' or ')' or '+' or '-' or '*' or '/':
#         return False
#     else: return True
#
#     # Create operand and operator stacks as empty stacks.
# OperandoStack = []
# OperadorStack = []
# exp = ["a", "+", "(", "b", "-", "c", "*", "d", "^", "e", ")", "/", "a"]
#     # While input expression still remains, read and process the next token.
#
# while not exp:  # read next token from the input expression
#     # Test if token is an operand or operator
#     if operando(exp[0]):
#         # Push operand onto the operand stack.
#         OperandoStack.Push(exp[0])
#     # If it is a left parentheses or operator of higher precedence than the last, or the stack is empty,
#     elif exp[0] is "(" or OperadorStack.IsEmpty() or OperatorHierarchy(exp[0]) > OperatorHierarchy(OperadorStack.Top()):
#     # push it to the operator stack
#         OperadorStack.Push( exp[0] )
#     elif exp[0] is ")":
#         #Continue to pop operator and operand stacks, building
#         #prefix expressions until left parentheses is found.
#         #Each prefix expression is push back onto the operand
#         #stack as either a left or right operand for the next operator.
#         while OperadorStack.Top() is not "(" :
#             OperadorStack.Pop(operator)
#             OperandoStack.Pop(RightOperand)
#             OperandoStack.Pop(LeftOperand)
#             operand = operator + LeftOperand + RightOperand
#             OperandoStack.Push(operand)
#         # Pop the left parthenses from the operator stack.
#         OperadorStack.Pop(operator)
#
#     elif operator hierarchy of token is less than or equal to hierarchy of top of the operator stack:
#     # Continue to pop operator and operand stack, building prefix
#     # expressions until the stack is empty or until an operator at
#     # the top of the operator stack has a lower hierarchy than that
#     # of the token.
#         while( !OperatorStack.IsEmpty() and OperatorHierarchy(token) lessThen Or Equal to OperatorHierarchy(OperatorStack.Top()) )
#             OperatorStack.Pop(operator)
#             OperandStack.Pop(RightOperand)
#             OperandStack.Pop(LeftOperand)
#             operand = operator + LeftOperand + RightOperand
#             OperandStack.Push(operand)
#         endwhile
#     # Push the lower precedence operator onto the stack
#     OperatorStack.Push(token)
#
#     # If the stack is not empty, continue to pop operator and operand stacks building
#     # prefix expressions until the operator stack is empty.
# while( !OperatorStack.IsEmpty() ) OperatorStack.Pop(operator)
#     OperandStack.Pop(RightOperand)
#     OperandStack.Pop(LeftOperand)
#     operand = operator + LeftOperand + RightOperand
#     OperandStack.Push(operand)
# endwhile
#
# # Save the prefix expression at the top of the operand stack followed by popping // the operand stack.
#
# print OperandoStack.Top()
#
# OperandoStack.Pop()







