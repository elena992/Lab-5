def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(6, 2))
    print(multiplicar(4, 4))
    print(dividir(8, 2))