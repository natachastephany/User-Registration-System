# Trabalho de Lógica de Programação II
# Turma 894 - <Div>ersidade Tech
# Professores: Henrique Assis Cordeiro e Alex Lima
# Membros do grupo:
#    Adriano Santana
#    Ana Beatriz Furtado
#    Natacha Stephany Sousa da Silva
#    Thammyres Valéria
#    Raphael Caetano da Silva

#Início - Importando a Biblioteca JSON 
import json

#Criação do path local manual
#path = 'C:/Users/Raphael/Dropbox/PC/Documents/Trabalho/DicionarioJSON.json' # -> Path local

#Abrir arquivo e copiar numa variável na memória para editar
#Criação do path de forma que o dicionário funcione se estiver no mesmo diretório que o programa.
arquivo = open('DicionarioJSON.json','r', encoding='utf-8')
dicionario = json.loads(arquivo.read())  #  --> Utilizar a variável 'dicionario' para fazer as alterações no DICIONÁRIO.
arquivo.close() # -> Fechar o arquivo para não atrapalhar o coleguinha

menu = """
#############################################################################################
##                  SISTEMA DE ADMINISTRAÇÃO DE CREDENCIAIS:                               ##        
##                                                                                         ##
##  1 - Inserir usuário                                                                    ##
##  2 - Excluir usuário                                                                    ##
##  3 - Atualizar usuário                                                                  ##
##  4 - Informações de um usuário                                                          ##
##  5 - Informações de todos os usuários VÁLIDOS                                           ##
##  6 - Inserir vários usuários                                                            ##
##  7 - Sair                                                                               ##
##                                                                                         ##
#############################################################################################

"""

#Funções 

#1) Função que checa a validade do ID do usuário
def checa_id():
    id_usuario = input("Insira o ID do usuário: ") 
    
    while id_usuario not in dicionario.keys():
        print('Usuário não encontrado!')
        id_usuario = input('Insira um outro ID: \n')
            
    while dicionario[id_usuario]['Status'] == False:
        print("Usuário já deletado")
        id_usuario = input('Insira um outro ID: \n')

  
    return id_usuario

#2) Função para inserir usuário
def inserir_usuario():
    #Pegar o último ID inserido
    lista = list(dicionario.keys())
    lista_num = [int(x) for x in lista]
    chave_nova = str(lista_num.pop() + 1)
    #Inserir Usuário
    nome = input("\n Digite o nome do novo usuario: ")
    while nome == '':
        nome = input("Inválido! Digite o nome do novo usuario: ")
    
    #Telefone e endereço podem ser adicionados sem parâmetro.
    telefone = input("Digite o telefone: ")
    if telefone == "":
        telefone = 'Não informado'
    
    endereco = input ("Digite o endereço: ")
    if endereco == "":
        endereco = 'Não informado'

    #dict.update({último ID: Valores})

    dicionario.update({chave_nova:
                                  {"Status":True,
                                    "Nome": nome,
                                    "Telefone" : telefone, 
                                    "Endereço" : endereco
                                    }
                                    })
    print(f"\n Usuário {dicionario[chave_nova]['Nome']} inserido com sucesso \n")
    print(f'Dados inseridos:')
    for chave, informacao in zip(dicionario[chave_nova].keys(), dicionario[chave_nova].values()):
        if chave != "Status":
            print(f"{chave}: {informacao}")

#3) Função para excluir (Alterar Status para False)
def excluir_usuario():      
      
    id_usuario = checa_id()
    if dicionario[id_usuario]['Status'] == True :
        dicionario[id_usuario]['Status'] = False
        print(f"Usuário {id_usuario}, {dicionario[id_usuario]['Nome']}, apagado com sucesso! ")
        
    excluir_outro = input("\n Deseja excluir outro usuario? \n 1 - Sim \n 2 - Não \n")
    if excluir_outro == '1':
            excluir_usuario()

#4) Função para inserir múltiplos usuários
def multiplos_usuarios():
    num = int(input("Qual a quantidade de usuários a ser salva no dicionário: "))
    for i in range(num):
        inserir_usuario()

#5) Função para exibir usuários válidos (Status:True)
def exibir_usuarios_validos(): 
    for id_usuario, valor in dicionario.items():
        if valor['Status'] == True:
            print()
            print(f'ID:{id_usuario}')
            for chave, informacao in zip(dicionario[id_usuario].keys(), dicionario[id_usuario].values()):
                print(f"{chave}: {informacao}")

#6) Função para alterar usuário (Alterar informações do usuário: Nome, Telefone, Endereço) 
def editar_usuario(id_usuario):
        
    #Primeiro, pede qual informação o usuario quer modificar
    escolha_edicao = input("Escolha qual categoria gostaria de mudar: \n 1 - Nome \n 2 - Telefone \n 3 - Endereço \n")
    escolhas = {'1': 'Nome', '2': 'Telefone', '3': 'Endereço'} #dicionário auxiliar com as opções
    
    #Verifica se a escolha está entre as opções
    while escolha_edicao not in escolhas.keys():
        print("Erro!")
        escolha_edicao = input("Escolha qual categoria gostaria de mudar: \n 1 - Nome \n 2 - Telefone \n 3 - Endereço \n")
    
    #Recebe a nova informação
    chave_dicionario = escolhas[escolha_edicao]
    dicionario[id_usuario][chave_dicionario] = input(f"Insira novo {chave_dicionario} \n ")
       
    #Informa ao usuário qual a nova informação do ID alterado
    for chave, informacao in zip(dicionario[id_usuario].keys(), dicionario[id_usuario].values()):
        if chave != "Status":
            print(f"{chave}: {informacao}")
            
    mudar_mais_algo = input("\n Deseja mudar mais alguma categoria? \n 1 - Sim \n 2 - Não \n")
    if mudar_mais_algo == '1':
        editar_usuario(id_usuario)

#7) Função para buscar um único usuário
def buscar():
    id_usuario = checa_id()           
    print(f"ID:{id_usuario}")
    for chave, informacao in zip(dicionario[id_usuario].keys(), dicionario[id_usuario].values()):
        print(f"{chave}: {informacao}")
    
    buscar_outro = input("\n Deseja buscar outro ID? \n 1 - Sim \n 2 - Não \n")
    if buscar_outro == '1':
        buscar() 

#8) Função para Salvar e sobrescrever o arquivo
def salva_e_fecha(dicionario):
    salvar_dados = json.dumps(dicionario, indent=4, ensure_ascii=False) # -> Convertendo o dicionário PYTHON em .JSON

    arquivo = open('DicionarioJSON.json', 'w', encoding='utf-8') # -> Abrindo o arquivo com permissão de escrita (APAGAR TUDO)
    arquivo.write(salvar_dados) # -> Salvando e sobrescrever o dicionário com os dados convertidos

    arquivo.close # -> Fechar a conexão com o arquivo


#Chamar o menu e escolher as opções
while True:
    print(menu)
    escolha = int(input("Digite uma opção: "))
    print()

    if escolha ==1:
        inserir_usuario()
    elif escolha ==2 :
        excluir_usuario()
    elif escolha ==3:
        id_usuario = checa_id()
        editar_usuario(id_usuario)
    elif escolha == 4:
        buscar()   
    elif escolha ==5 :
        exibir_usuarios_validos()
    elif escolha ==6 :
        multiplos_usuarios()
    elif escolha ==7:
        salva_e_fecha(dicionario)
        break

