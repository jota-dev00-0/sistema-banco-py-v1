saldo = 0
limite_saque_diario = 500
saques = 0
LIMITE_SAQUE = 3
extrato = ""

    
def menu ():
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
    valor = float(input("digite o valor que deseja depositar")) 
    global saldo, extrato
    if valor > 0:    
        saldo += valor
        extrato += f"\ndeposito feito no valor de {valor:.2f}"
        print(f"saldo atual: {saldo}")
        
        
    else:
        print("digite um valor maior que zero por favor ")
        

def sacar ():
    valor = float(input("digite o valor que deseja sacar"))
    
    global saldo, extrato, saques
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saque_diario
    excedeu_saques = saques >= LIMITE_SAQUE
    
    if excedeu_saldo:
        print("sua transacao passa o limite")
        
    elif excedeu_saques:
        print("limite de saques atingidos")
        
    elif excedeu_limite:
        print("limite de valor de saque atingido")
    
    elif valor <= 0:
        print("digite um valor ")
    
    if(valor > 0 and not excedeu_limite):
        saldo -= valor
        extrato += f"\nsaque efetuado no valor de {valor:.2f}"
        saques += 1
        print(f"saldo atual: {saldo:.2f}")
        
    else:
        print("operacao falhou!")
        
def exibir_extrato ():
    print("======Extrato======")
    print("nao foram realizadas movimentacoes" if not extrato else extrato)
    print(f"\nsaldo atual {saldo:.2f}R$")
    

menu()