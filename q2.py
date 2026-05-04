#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.



while True:
    user = input("Digite o nome de úsuario: ")
    senha = input("Digite sua senha: ")
    if user == senha:
        print("A senha não pode ser a mesma que o úsuario.")
        if user == senha:
            print("Tente novamente.")
        else:
            print("Úsuario cadastrado com sucesso.")
            break