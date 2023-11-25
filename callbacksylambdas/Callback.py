def imprimir(valor):
    print(valor)


def calcular_area(base, altura, imprimir):
    area = base*altura
    imprimir(area)


base = 50
altura = 5

calcular_area(base, altura, imprimir)

salario = float(input("Ingresa el valor del salario:"))

def aux_trans(salario, pago_neto):
    if(salario< 2320000):
        print(f"salario neto if : {pago_neto + 140606}")
    else:
        print(f"salario neto else: {pago_neto}")

def pago_neto(salario, aux_trans):
    eps = lambda salario: salario * 0.04
    pension = lambda salario: salario * 0.04
    pago_neto = salario - eps(salario) - pension(salario)
    aux_trans(salario, pago_neto)

pago_neto(salario, aux_trans)







