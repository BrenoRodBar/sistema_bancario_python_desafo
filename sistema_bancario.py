menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

    
    
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        d = float(input("Digite o valor a ser depositado: "))
        while d < 1:
            d = float(input("O deposito não pode ser menor que R$ 1,00"))
        saldo = saldo + d
        extrato.append(f"Você fez um deposito no valor de: R${d:.2f}")

    elif opcao == "s":
        print("Saque")
        if numero_saques > LIMITE_SAQUES:
            print("Você atingiu o limite de saques diarios(3).")

        elif saldo == 0:
            print("Você não tem saldo suficiente para sacar este valor.")
        
        else:
            s = float(input("Digite o valor do saque: "))
            while s > 500:
                s = float(input("O limite por saque é de R$500.00, por favor, digite uma quantia menor."))
                
            saldo = saldo - s
            extrato.append(f"Você fez um saque no valor de: R${s:.2f}")
            numero_saques = numero_saques + 1
    elif opcao == "e":
        print("Extrato")
        if not extrato:
            print("Não foram realizadas movimentações nesta conta.")
        else:
            for i in extrato:
                print(i)
            print(f"O saldo atual é: R${saldo:.2f}")   
    elif opcao == "q":
        break
