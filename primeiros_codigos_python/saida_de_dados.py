print("Bom dia", end = '') # o end faz que seja impresso os dois valores na mesma linha
print("Boa noite")

#####################################
x = "maria"
y = 19

print("%s tem %d anos" %(x, y))


#####################################
idade: int
salario: float
nome: str
sexo: str

idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f"\nA funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))


#casting

a: int; b: int; resultado: int
a = 5
b = 2
resultado = a / b #ou pode usar '//' para ser calculado o valor inteiro
print(resultado)
