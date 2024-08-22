import os
from datetime import datetime, timedelta, date

Nome_Usuario = []
Cad_Usuario_Novo = []
Cad_Idade = []
Financiamento_Banco_Veic_Novo = [{'Banco':'Bradesco', 'Tx_juros':'1,58/100'},{'Banco':'caixa', 'Tx_juros':'1,58/100'}]

Financiamento_Banco_Veic_Usado = [{'Banco':'Bradesco', 'Tx_juros': '3,58/100'},
                                  {'Banco': 'Caixa Economica', 'Tx_juros': '3,85/100'}]


def Nome_programa():
   #função mostra o nome do programa
    print('\nSeja bem vindo ao restaurante Rodrigo Lima\n')

def Cadas_Usuario():
    #função recebe nome do usuario e salva na lista Nome_usuario
    if not Nome_Usuario:
        print("Qual o seu nome?")
        Nome = str(input()).strip().title()
        Nome_Usuario.append(Nome)
    else:
        pass

def Menu_principal():
    os.system('cls')
    print('Seja bem vindo {}'.format(Nome_Usuario[0]))
    print('''
    [1] Cadastro Cliente
    [2] Emprestimo
    [3] Financiamento
    [4] Sair''')

def Escolha_Do_Usuario():
    # função salva escolha do menu principal
    escolha = str(input('')).strip()
    escolha = int(escolha)
    if escolha == 1:
        os.system('cls')
        Cadastro_Completo()
    elif escolha == 2:
        os.system('cls')
        Emprestimo()
    elif escolha == 3:
        os.system('cls')
        Financiamento()
    elif escolha == 4:
        os.system('cls')
        print('Tem certeza que deseja sair?\n Sim\nNão')
        sair = str(input()).strip().upper()
        if sair == "NÃO":
            main()
        else:
            print('até logo!')
            os.system('cls')
            exit()

    else:
        os.system('cls')
        print('Escolha uma opção valida\n Aperte qualquer botão para voltar ao menu principal')
        input()
        main()

def Cadastro_Completo():
    os.system('cls')
    print("Qual o nome seu nome completo?")
    Cad_Nome_completo = str(input()).strip().title()
    Cad_Usuario_Novo.append(Cad_Nome_completo)
    Idade()

def Juros_Maior_33anos():
    Valor_Emprestimo = float(input('qual o valor desejado?'))
    Quantidade_parcelas = int(input('quantos meses você deseja financiar'))
    print('calculando + 33 anos...')
    juros_mes = 0.99 / 100
    Montante = Valor_Emprestimo + (Valor_Emprestimo * juros_mes * Quantidade_parcelas)
    Valor_da_parcela = Montante / Quantidade_parcelas
    print('O valor solicitado é R${}, ao final de {} parcelas, você irá pagar o total de R${} e sua parcela será de R${}'.format(Valor_Emprestimo, Quantidade_parcelas, Montante, Valor_da_parcela))
    input()

def Juros_Menor_33anos():
    Valor_Emprestimo = float(input('qual o valor desejado?'))
    Quantidade_parcelas = int(input('quantos meses você deseja financiar'))
    print('calculando - 33 anos ...')
    print('o valor do emprestimo é{}'.format(Valor_Emprestimo))
    juros_mes = 1.29/100
    Montante = Valor_Emprestimo + (Valor_Emprestimo * juros_mes * Quantidade_parcelas)
    Valor_da_parcela = Montante / Quantidade_parcelas
    print('O valor solicitado é R${} ao final de {} parcelas você irá pagar o total de R${}'.format(Valor_Emprestimo, Quantidade_parcelas, Montante))
    input()

def Emprestimo ():
    os.system('cls')
    print('Emprestimo\n')
    if len(Cad_Usuario_Novo) == 0:
        print('Faça o cadastro primeiro. \nAperte qualquer tecla para voltar ao menu principal. \n\n')
        input()
        os.system('cls')
        main()

    else:
        idade = Cad_Idade



        if idade[0] >= 33:
            Juros_Maior_33anos()


        else:
            Juros_Menor_33anos()

def Financiamento():
    os.system('cls')
    global Escolha_Financiamento
    print('Financiamento\n')
    print('''
        [1] Financiamento Veiculo
        [2] Financiamento Imovel
        [3] Financiamento Estudantil
        [4] Sair''')
    Escolha_Financiamento = int(input())
    Financiamento_Escolha()

def Financiamento_Escolha():
    if Escolha_Financiamento == 1:
        os.system('cls')
        Financiamento_Veiculo()
    elif Escolha_Financiamento == 2:
        os.system('cls')
        Financiamento_Imovel()
    elif Escolha_Financiamento == 3:
        os.system('cls')
        Financiamento_Estudantil()
    elif Escolha_Financiamento == 4:
        os.system('cls')
        print('Tem certeza que deseja sair?\n Sim\nNão')
        sair = str(input()).strip().upper()
        if sair == "NÃO":
            main()
        else:
            print('até logo!')
            os.system('cls')
            exit()

def Financiamento_Veiculo():
    os.system('cls')
    print('Olá {}, seja bem vindo \nFinanciamento veiculo'.format(Nome_Usuario[0]))
    Tipo_Financiamento = int(input('Qual tipo de finaciamento você deseja?\n[1]Veiculo Novo\n[2]Veiculo Usado\n'))
    if Tipo_Financiamento == 1:
        Financiamento_Veiculo_Novo()
    elif Tipo_Financiamento == 2:
        Financiamento_Veiculo_Usado()
    else:
        print('Escolha uma opção valida!\nAperte qualquer tecla para voltar!')
        input()
        Financiamento_Veiculo()



def Financiamento_Veiculo_Novo():
    for Banco in Financiamento_Banco_Veic_Novo:
        Nome_Banco = Banco['Banco']
        print(f' - {Nome_Banco}')


Financiamento_Veiculo_Novo()

def Financiamento_Veiculo_Usado():
    pass
def Financiamento_Imovel():
    print('Olá {}, seja bem vindo \nFinanciamento Imovel'.format(Nome_Usuario))
    input()
def Financiamento_Estudantil():
    print('Olá {}, seja bem vindo \nFinanciamento Estudantil'.format(Nome_Usuario))
    input()




def Idade():
    Ano_nascimento = int(input('Qual o ano de nascimento (aaaa)\n'))
    if Ano_nascimento >= 1900:
        data = datetime.now()
        ano = data.strftime('%y')
        data_ano = int(ano) + 2000
        idade =  data_ano - Ano_nascimento
        Cad_Idade.append(idade)
        print('Cadastro realizado com sucesso!\nAperte qualquer tecla para volar ao menu principal')
        input()
        main()
    else:
        print('Atenção, escolha um ano com 4 digitos (aaaa)\n')
        Idade()

def main():
    os.system('cls')
    Nome_programa()
    Cadas_Usuario()
    Menu_principal()
    Escolha_Do_Usuario()
if __name__ ==  '__main__':
    main()