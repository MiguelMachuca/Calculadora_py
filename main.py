from notaciones import *


# exp = ["a", "+", "(", "b", "-", "c", "*", "d", "^", "e", ")", "/", "a"]

def PreordenReconstruccion(P, I):
    if len(I) == 0 or len(P) == 0:
        return
    else:
        Izquierda = []
        Derecha = []
        x = 0
        Raiz = P[0]
        while I[x] != Raiz:
            Izquierda.append(I[x])
            x = x + 1
        Derecha = I[x + 1:len(I)]
        print(Izquierda, "<-", Raiz, "->", Derecha)

        PreordenReconstruccion(P[1:len(Izquierda) + 1], Izquierda)
        PreordenReconstruccion(P[len(P) - len(Derecha):len(P)], Derecha)


def main():
    exp = "(52 + 88 * 46) + (300 - 734)"
    notacion = notationConversion(exp)
    print(notacion.infixToPrefix())
    print(notacion.sinCorchetes())
    PreordenReconstruccion(notacion.infixToPrefix(), notacion.sinCorchetes())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
