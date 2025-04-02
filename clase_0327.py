class Vector:
    def __init__(self, iterable):
        self._vector = [elemento for elemento in iterable]

    def __repr__(self):
        return f"vector({self._vector})"

    def __str__(self):
        cadena = "[ "
        for elemento in self._vector:
            cadena += f"{elemento}"
        cadena += " ]"
        return cadena

    def __getitem__(self, index):
        return self._vector[index]

    def __setitem__(self, index, valor):
        self._vector[index] = valor

    def __len__(self):
        return len(self._vector)

    def __add__(self, otro):
        if isinstance(otro, (int, float, complex)):
            return Vector([elemento + otro for elemento in self._vector])
        else:
            return Vector([num1 + num2 for num1, num2 in zip(self, otro)])


    __radd__ = __add__

