# tab1 = int(input("Digite um número"))
# for n in range(11):
#     print(f'{tab1} X {tab1} = {tab1 * n}')


numero = int(input("Digite um número para ver a tabuada: "))
inicio = int(input("Digite o número inicial da tabuada: "))
fim = int(input("Digite o número final da tabuada: "))

alinhamento = input("Deseja alinhar os resultados à direita? (s/n): ")

print(f"Tabuada do {numero}")
for i in range(inicio, fim+1):
    if alinhamento.lower() == 's':
        print(f"{numero} x {i:2} = {numero * i:>3}")
    else:
        print(f"{numero} x {i} = {numero * i}")