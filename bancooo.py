from datetime import datetime

saldo = 0
limite_saque_diario = 500
saques = 0
LIMITE_SAQUE = 3
extrato = ""
LIMITE_TRANSACOES_DIARIAS = 10
transacoes_hoje = 0
depositos = 0
    
def menu():
    while True:
        option = input("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """).strip().lower()
        match option:
            case "d":
                depositar()
            case "s":
                sacar()
            case "e":
                exibir_extrato()
            case "q":
                break
        
def depositar():
    global saldo, extrato, transacoes_hoje, depositos
    
    if transacoes_hoje >= LIMITE_TRANSACOES_DIARIAS:
        print("Limite diário de transações atingido (10 transações).")
        return
        
    valor = float(input("Digite o valor que deseja depositar: ")) 
    
    if valor > 0:    
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"\n{data_hora} - Depósito: R$ {valor:.2f}"
        transacoes_hoje += 1
        depositos += 1
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Digite um valor maior que zero por favor.")

def sacar():
    global saldo, extrato, saques, transacoes_hoje
    
    if transacoes_hoje >= LIMITE_TRANSACOES_DIARIAS:
        print("Limite diário de transações atingido (10 transações).")
        return
        
    valor = float(input("Digite o valor que deseja sacar: "))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saque_diario
    excedeu_saques = saques >= LIMITE_SAQUE
    
    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_saques:
        print("Limite diário de saques atingido (3 saques).")
    elif excedeu_limite:
        print(f"Valor máximo por saque: R$ {limite_saque_diario:.2f}")
    elif valor <= 0:
        print("Digite um valor positivo.")
    else:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"\n{data_hora} - Saque: R$ {valor:.2f}"
        saques += 1
        transacoes_hoje += 1
        print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")

def exibir_extrato():
    print("\n" + "="*20 + " EXTRATO " + "="*20)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("="*50)

menu()

# va

