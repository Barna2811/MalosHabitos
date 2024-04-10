def calcular(a, b, c):
    return a * b + c

def principal():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))

    resultado = calcular(a, b, c)
    print("El resultado es:", resultado)

principal()
