class MiIterador:
    def __init__(self, max_num):
        self.max_num = max_num
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual < self.max_num:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            raise StopIteration

# Usando el iterador personalizado
mi_iterador = MiIterador(5)
for num in mi_iterador:
    print(num)
