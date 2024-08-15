import os
from datetime import datetime, timedelta, date

Nome_Usuario = ['dd']
Cad_Usuario_Novo = ['ss']
Cad_Idade = [33]

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
    print('Seja bem vindo {}'.format(Nome_Usuario))
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
        print('Financiamento')
    elif escolha == 4:
        os.system('cls')
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
    global  juros_mes_maior
    juros_mes_maior = 0.99/100

def Juros_Menor_33anos():
    juros_mes = 1.29/100

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
        Valor_Emprestimo = float(input('qual o valor desejado?'))
        Quantidade_parcelas = int(input('quantos meses você deseja financiar'))
        Valor_parcela = (Valor_Emprestimo / Quantidade_parcelas)
        print(Valor_parcela)

        if idade[0] >= 33:
            print('passou')
            Juros_Maior_33anos()
            #Valor_parcela_juros = Valor_parcela * Quantidade_parcelas * juros_mes_maior
            #print('o valor da parcela é {}'.format(Valor_parcela_juros))
            #input()
            #main()




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