pila = []
exp = ["a", "+", "(", "b", "-", "c", "*", "d", "^", "e", ")", "/", "a"]

print("Infijo: ")
print(exp)
print("Prefijo: ")

for i in range(0, 13):
    if exp[i] == 'a' or exp[i] == 'b' or exp[i] == 'c' or exp[i] == 'd' or exp[i] == 'e' or exp[i] == '(':
        pila.append(exp[i])
    if exp[i] == '+' or exp[i] == "-" or exp[i] == '*' or exp[i] == '/' or exp[i] == '^':
        print(str(exp[i]) + " ")
    if exp[i] == ')':
        if pila:
            dato = pila.pop()
            while pila and dato != "(":
                print(str(dato) + " ")
                dato = pila.pop()
print(pila)

