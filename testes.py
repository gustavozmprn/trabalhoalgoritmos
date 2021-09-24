usuarios = []
usuarios_raw = []
creditos = []
class usuario:
    usuario: None
    senha: None
    email: None
    cpf: None
def ler_usuarios():
    with open('usuarios_1.txt','r',newline='') as arquivo:         #LER ARQUIVO TXT
        for linha in arquivo:
            linha = linha.strip(",")
            usuarios.append(linha.split())
def adicionar_usuarios():                       #ADICIONAR INFOS AO ARQUIVO TXT
    with open('usuarios_1.txt','a',newline='') as arquivo:
        for i in usuarios_raw:
            arquivo.write(str(i.usuario)+ ' ' + str(i.senha) + ' ' + str(i.email) + ' ' + str(i.cpf) + '\n')
def registro():    
    print("\n-----------REGISTRO-----------\n")        #Começo do registro
    a = 0
    soma = 0
    for i in range(1):
        registro = usuario()
        while True:
            registro.usuario = input("Digite seu usuário: ")
            while True:
                if registro.usuario == "":
                    registro.usuario = input("Digite seu usuário, sem deixar em branco: ")
                else:
                    break
            if teste_usuario(registro.usuario):
                break
        while True:
            registro.senha = input("Digite sua senha: ")
            if registro.senha == "":
                print("Não deixe sua senha em branco")
            else:
                while True:                                 #Verificar se senha e usuario são iguais
                    if registro.usuario == registro.senha:
                        print("Senha e usuário não podem ser iguais, tente novamente")
                        registro.senha = input("Digite outra senha: ")
                    else:
                        break
                break
        while True:
            registro.email = input("Digite seu email: ")
            while True:                                 #Verificar se e-mail é valido
                if not "@" in list(registro.email):
                    print("e-mail invalido")
                    registro.email = input("Digite seu email: ")
                else:
                    break 
            if teste_email(registro.email):
                break
        while True:
            while True:                                 #Adicionar CPF e verificar se é válido ou não
                registro.cpf = input("Digite seu CPF: ")
                if cpf_verdadeiro(registro.cpf):
                    break
                else:
                    print("CPF inválido, tente novamente")
            if teste_cpf(registro.cpf):
                break
        print("\n-=|Usuario Registrado|=-\n")
        usuarios_raw.append(registro)
        adicionar_usuarios()
        ler_usuarios()
def login():
    print("\n-------------LOGIN-------------\n")
    global usuario
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    x = 0
    while x<1:
        for i in range(len(usuarios)):
            if usuario == usuarios[i][0] and senha == usuarios[i][1]:
                print("\nLogin realizado com sucesso\n")
                x += 1
                return True
            else:
                pass
        pergunta = int(input("Usuário não cadastrado, tente novamente(1) ou registre-se(2): "))
        if pergunta == 1:
            usuario = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")
        elif pergunta == 2:
            registro()
def operacoes():                                    #Tabelas
    print("\n-------------COMPRA-------------\n")
    x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    y = [0.00,2.00,3.50,6.30,12.00,22.00,10.50,1.50,50.00,45.00,150.00,5.00,75.00,20.00,7.50,0.50]
    a = 0
    b = 0
    credito_invalido_a = 0
    credito_invalido_b = 0
    credito = 1000                                      #Credito inicial
    tabela = f"""Produto | ID |Preço | Quantidade       
Arroz   | 1  | {y[1]}  |     {x[1]}
Arroz   | 2  | {y[2]}  |     {x[2]}
Arroz   | 3  | {y[3]}  |     {x[3]}
Arroz   | 4  | {y[4]} |     {x[4]}
Arroz   | 5  | {y[5]} |     {x[5]}
Arroz   | 6  | {y[6]} |     {x[6]}
Arroz   | 7  | {y[7]}  |     {x[7]}
Arroz   | 8  | {y[8]} |     {x[8]}
Arroz   | 9  | {y[9]} |     {x[9]}
Arroz   | 10 | {y[10]}|     {x[10]}
Arroz   | 11 | {y[11]}  |     {x[11]}
Arroz   | 12 | {y[12]} |     {x[12]}
Arroz   | 13 | {y[13]} |     {x[13]}
Arroz   | 14 | {y[14]}  |     {x[14]}
Arroz   | 15 | {y[15]}  |     {x[15]}"""
    while True:                                        #Adicionar valores
        print(f"\n Seu credito restante é igual a: {credito}")
        print(tabela)
        a = int(input("Digite o ID do produto ou 0(duas vezes) para finalizar a operação: "))
        b = int(input("Quantidade do produto selecionado: "))
        if a != 0 and credito > 0:
            x[a] = x[a] + b
            credito = credito - y[a] * b
            tabela = f"""Produto | ID |Preço | Quantidade
Arroz   | 1  | {y[1]}  |     {x[1]}
Arroz   | 2  | {y[2]}  |     {x[2]}
Arroz   | 3  | {y[3]}  |     {x[3]}
Arroz   | 4  | {y[4]} |     {x[4]}
Arroz   | 5  | {y[5]} |     {x[5]}
Arroz   | 6  | {y[6]} |     {x[6]}
Arroz   | 7  | {y[7]}  |     {x[7]}
Arroz   | 8  | {y[8]} |     {x[8]}
Arroz   | 9  | {y[9]} |     {x[9]}
Arroz   | 10 | {y[10]}|     {x[10]}
Arroz   | 11 | {y[11]}  |     {x[11]}
Arroz   | 12 | {y[12]} |     {x[12]}
Arroz   | 13 | {y[13]} |     {x[13]}
Arroz   | 14 | {y[14]}  |     {x[14]}
Arroz   | 15 | {y[15]}  |     {x[15]}"""
        elif credito < 0:
            credito_invalido_a = int(input("Crédito negativo, necessitamos que remova alguns produtos,\ndigite o ID do produto: "))
            credito_invalido_b = int(input("Digite a quantidade de produtos removidos desejada: "))
            credito = credito + y[credito_invalido_a] * credito_invalido_b
            x[credito_invalido_a] = x[credito_invalido_a] - credito_invalido_b
            tabela = f"""Produto | ID |Preço | Quantidade
Arroz   | 1  | {y[1]}  |     {x[1]}
Arroz   | 2  | {y[2]}  |     {x[2]}
Arroz   | 3  | {y[3]}  |     {x[3]}
Arroz   | 4  | {y[4]} |     {x[4]}
Arroz   | 5  | {y[5]} |     {x[5]}
Arroz   | 6  | {y[6]} |     {x[6]}
Arroz   | 7  | {y[7]}  |     {x[7]}
Arroz   | 8  | {y[8]} |     {x[8]}
Arroz   | 9  | {y[9]} |     {x[9]}
Arroz   | 10 | {y[10]}|     {x[10]}
Arroz   | 11 | {y[11]}  |     {x[11]}
Arroz   | 12 | {y[12]} |     {x[12]}
Arroz   | 13 | {y[13]} |     {x[13]}
Arroz   | 14 | {y[14]}  |     {x[14]}
Arroz   | 15 | {y[15]}  |     {x[15]}"""
        elif a == 0:
            credito = 1000
            print("\n---------Operação finalizada, crédito zerado---------\n")
            while True:
                desejo = int(input("1 para continuar operações, 2 para voltar para o menu principal: \n"))
                if desejo == 1:
                    break
                elif desejo == 2:
                    menu()
                elif desejo != 1 and desejo != 2:
                    desejo = int(input("1 para continuar operações, 2 para voltar para o menu principal: \n"))


                
def menu():                                      #Opções bases de tudo
    questao = int(input("Opções: \n1: Login\n2: Registro\n3: Sair\nQue operação deseja? \n"))
    if questao == 1:
        if login():
            questao2 = int(input("Deseja efetuar operações de compra? 1-Sim 2-Não: \n"))
            if questao2 == 1:
                operacoes()
            if questao2 == 2:
                print("Ok, redirecionando para o menu")
                menu()
    if questao == 2:
        registro()
        if login():
            questao3 = int(input("Deseja efetuar operações de compra? 1-Sim 2-Não: \n"))
            if questao3 == 1:
                operacoes()
            if questao3 == 2:
                print("Ok, redirecionando para o menu")
                menu()
    if questao ==3:
        print()
        exit()
def teste_usuario(user):                                        #TESTANDO SE USUARIO JA EXISTE NA DATABASE
    x = 0
    for i in range(len(usuarios)):
        if usuarios[i][0] == user:
            print("Usuário existente, tente novamente")
            return False
        else:
            x += 1
    if x == len(usuarios):
        x = 0
        return True
def teste_email(email):                                         #TESTANDO SE EMAIL JÁ EXISTE NA DATABASE
    x = 0
    for i in range(len(usuarios)):
        if usuarios[i][2] == email:
            print("Email existente, tente novamente")
            return False
        else:
            x+=1
    if x == len(usuarios):
        x = 0
        return True 
def teste_cpf(cpf):                                             #TESTANDO SE CPF JÁ EXISTE NA DATABASE
    x = 0
    for i in range(len(usuarios)):
        if usuarios[i][3] == cpf:
            print("CPF já utilizado, tenta novamente")
            return False
        else:
            x += 1
    if x == len(usuarios):
        x = 0
        return True
def cpf_verdadeiro(cpf):                                        #VERIFICANDO SE CPF É VERDADEIRO
    cpf_separado = list(str(cpf))
    x = 10
    y = 11
    primeiro_raw = 0
    segundo_raw = 0
    total = 0
    cpf_lista = list(cpf)
    cpf_remover_ultimo = cpf_lista.pop(10)
    cpf_remover_ultimo_dois = cpf_lista.pop(9)
    for i in cpf_lista:
        primeiro_raw = primeiro_raw + int(i) * x        #primeiro digito
        x -= 1
    primeiro_dividindo = primeiro_raw // 11
    primeiro_sobra = primeiro_raw % 11
    if primeiro_sobra < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - primeiro_sobra
    cpf_lista.append(str(primeiro_digito))
    for j in cpf_lista:
        segundo_raw = segundo_raw + int(j) * y
        y -= 1
    segundo_dividindo = segundo_raw // 11
    segundo_sobra = segundo_raw % 11
    if segundo_sobra < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_sobra
    cpf_lista.append(str(segundo_digito))
    for i in range(len(cpf_lista)):
        if cpf_separado[i] == cpf_lista[i]:
            total += 1
    if total == 11:
        return True
ler_usuarios()
menu()