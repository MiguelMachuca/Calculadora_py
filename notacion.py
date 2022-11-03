class GFG:
    @staticmethod
    def isalpha(c):
        if (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z'):
            return True
        return False

    @staticmethod
    def isdigit(c):
        if (c >= '0' and c <= '9'):
            return True
        return False

    @staticmethod
    def isOperator(c):
        return (not GFG.isalpha(c) and not GFG.isdigit(c))

    @staticmethod
    def getPriority(C):
        if (C == '-' or C == '+'):
            return 1
        elif (C == '*' or C == '/'):
            return 2
        elif (C == '^'):
            return 3
        return 0

    # Reverse the letters of the word
    @staticmethod
    def reverse(strg, start, end):
        # Temporary variable to store character
        temp = ' '
        while (start < end):
            # Swapping the first and last character
            temp = strg[start]
            strg[start] = strg[end]
            strg[end] = temp
            start += 1
            end -= 1
        return "".join(strg)

    @staticmethod
    def infixToPostfix(infix1):
        print(infix1)
        infix = str('(') + "".join(infix1) + str(')')
        l = len(infix)
        char_stack = []
        output = ""
        i = 0
        while (i < l):
            # If the scanned character is an
            # operand, add it to output.
            if (GFG.isalpha(infix[i]) or GFG.isdigit(infix[i])):
                output += infix[i]
            elif (infix[i] == '('):
                char_stack.append('(')
            elif (infix[i] == ')'):
                while (char_stack[-1] != ord('(')):
                    output += char_stack[-1]
                    char_stack.pop()
                # Remove '(' from the stack
                char_stack.pop()
            else:
                if (GFG.isOperator(char_stack[-1])):
                    while ((GFG.getPriority(infix[i]) < GFG.getPriority(char_stack[-1])) or (
                            GFG.getPriority(infix[i]) <= GFG.getPriority(char_stack[-1]) and infix[i] == '^')):
                        output += char_stack[-1]
                        char_stack.pop()
                    # Push current Operator on stack
                    char_stack.append(infix[i])
            i += 1
        while (not (len(char_stack) == 0)):
            output += char_stack.pop()
        return output

    @staticmethod
    def infixToPrefix(infix):
        # 		* Reverse String Replace ( with ) and vice versa Get Postfix Reverse Postfix *
        l = len(infix)
        # Reverse infix
        infix1 = GFG.reverse(infix, 0, l - 1)
        infix = list(infix1)
        # Replace ( with ) and vice versa
        i = 0
        while (i < l):
            if (infix[i] == '('):
                infix[i] = ')'
                i += 1
            elif (infix[i] == ')'):
                infix[i] = '('
                i += 1
            i += 1
        prefix = GFG.infixToPostfix(infix)
        # Reverse postfix
        prefix = GFG.reverse(list(prefix), 0, l - 1)
        return prefix

    # Driver code
    @staticmethod
    def main(args):
        s = ("x+y*z/w+u")
        print(GFG.infixToPrefix(list(s)), end="")


