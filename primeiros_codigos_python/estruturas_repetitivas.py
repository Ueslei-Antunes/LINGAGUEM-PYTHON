x: int
soma: int

soma = 0

x = int(input("Digite o primeiro numero: "))

for i in range(0, x):
    x = int(input("Digite outro numero: "))
    soma = soma + x

#while x != 0:
#    soma = soma + x
#    x = int(input("Digite outro numero: "))

print("SOMA = ", soma)


##############################################