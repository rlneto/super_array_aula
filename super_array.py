class SuperArray:
    def __init__(self, ini, fim):
        if fim >= ini:
            self.__linf = ini
            self.__lsup = fim
        else:
            self.__linf = fim
            self.__lsup = ini

        self.__dados = [None] * (self.__lsup - self.__linf + 1)

    def atribuir(self, pos, val):
        if (pos > self.__lsup) or (pos < self.__linf):
            raise IndexError
        else:
            self.__dados[pos - self.__linf] = val

    def acessar(self, pos):
        if (pos > self.__lsup) or (pos < self.__linf):
            raise IndexError
        else:
            return self.__dados[pos - self.__linf]


array1 = SuperArray(5, 2)
print(array1.acessar(2))
print(array1.acessar(3))
print(array1.acessar(4))
print(array1.acessar(5))


class SuperMatriz:
    def __init__(self, nl, nc):
        self.__mat = SuperArray(0, ((nl * nc) - 1))

    def atribuir(self, l, c, val):
        pass

    def acessar(self, l, c):
        pass
