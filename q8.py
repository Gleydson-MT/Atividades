# 12. Desenvolva um gerador de tabuada, capaz de gerar uma tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:



numero = int(input("Digite um número entre 1 e 10: "))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido! Digite um valor entre 1 e 10.")