#28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um

qtd_cds = int(input("Digite quantos cds foram adqueridos: "))
valor_cds = 0

for i in range(1):
    while True:
        if qtd_cds == 0:
            print("DIGITE UM VALOR VÁLIDO!")
        else:
            valor_cada_cd = float(input("Digite o valor pago nos CDs: "))
            valor_cds += valor_cada_cd 
            break
media = valor_cds/qtd_cds

print(f"Valor pago por cd em média foi de {media}")