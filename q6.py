#14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

qtd_pares = 0
qtd_impar = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if num %2 ==0:
        qtd_pares +=1
    if num %2 != 0:
        qtd_impar +=1
else:
    print(f"Há {qtd_pares}, números pares e {qtd_impar}, números impar.")