import os

def funcaoAlert(variavel):
    while(variavel == ""):
      print("\033[0;31mEste é um campo obrigatório!\033[m")
      variavel = input("Por favor preencha-o corretamente: ")
      return variavel

#Cadastra o cliente
def funcaoCadastra():

  banco = open("database.txt", "a", encoding="utf-8")

  insereCliente = input("Insira o nome do titular: ")
  funcaoAlert(insereCliente)

  insereCpf = input("Insira o cpf do titular: ")
  validaCpf = len(insereCpf)
  while (validaCpf < 11) or (validaCpf > 11):
    funcaoAlert(insereCpf)
    print("\033[0;31mCampo incorreto!\033[m")
    insereCpf = input("Por favor digite o CPF corretamente: ")
    validaCpf = len(insereCpf)
  
  numeroPessoas = input("Insira o número de pessoas: ")
  funcaoAlert(numeroPessoas)

  tipoQuarto = input("Insira o tipo do quarto: ")
  while((tipoQuarto != "S") and (tipoQuarto != "s") and (tipoQuarto != "D") and (tipoQuarto != "d") and (tipoQuarto != "P") and (tipoQuarto != "p")):
    funcaoAlert(tipoQuarto)
    print("\033[0;31mCampo incorreto!\033[m")
    tipoQuarto = input("Os tipos de quartos são S, D ou P, por favor insira um destes: ")

  numeroDias = input("Insira o numero de dias da reserva: ")

  nPessoas = int(numeroPessoas)
  nDias = int(numeroDias)

  #calcula o valor total da diaria

  if tipoQuarto == "S" or "s":
    valorQuarto = 100

  elif tipoQuarto == "D" or "d":
    valorQuarto = 200

  elif tipoQuarto == "P" or "p":
    valorQuarto = 300

  #calcula o valor total da diaria

  valor = nPessoas * nDias * valorQuarto

  status = ["R","A""C","F"]

  #insere o cadastro no banco

  banco.writelines("Nome: {}; CPF: {}; Número de pessoas hospedadas: {}; Tipo de quarto: {}; Dias de hospedagem: {}; Valor total: {}; Status: {}".format(insereCliente,insereCpf,numeroPessoas,tipoQuarto,numeroDias,valor,status[0]) + "\n")
  
  banco.close()
  
  print("Cadastro concluído com sucessso!")

def funcaoBusca():
    arquivo = open("database.txt", "r")
    listaClientes = arquivo.readlines()
    arquivo.close

    novaLista = []
    for dados in listaClientes:
        nome,cpf,nPessoas,tipoQuarto,nDias,valor,status = dados.split(";")
        clientes = {"nome" : nome, "cpf" : cpf, "nPessoas" : nPessoas, "tipoQuarto" : tipoQuarto, "valor" : valor, "nDias" : nDias, "status" : status}
        novaLista.append(clientes)
    return novaLista


def funcaoAltera(DadosAtt):
    arquivo = open("database.txt", "w")
    for i in DadosAtt:
        arquivo.write(f"{i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    arquivo.close

#Entrada de cliente
def funcaoCheckIn():
    cpf = input("Procurar por cpf: ")
    novaLista = funcaoBusca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    reservaEsc = input(int(input("Escolha a reserva: ")))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                i['status'] = "A"
    funcaoAltera(novaLista)
    print("Check in realizado com sucesso!!")

def alterar_linha(arquivo,nLinha,novalinha):
    with open(arquivo,'r') as f:
        texto=f.readlines()
    with open(arquivo,'w') as f:
        for i in texto:
            if texto.index(i) == nLinha:
                f.write(novalinha +'\n')
            else:
                f.write(i)

# def funcaoCheckIn():
#   with open("database.txt", "r") as banco:
#     lista = banco.readlines()
#   with open('database.txt', 'w') as banco:
#       cpf = input("cpf aq: ")
#       for cpf in lista:
#         if lista.index(cpf) == 1:
#           banco.write("Nome: teste; CPF: teste; Número de pessoas hospedadas: teste; Tipo de quarto: teste; Dias de hospedagem: teste; Valor total: teste; Status: teste" + "\n")
          
#         else:
#           banco.write(lista)
    
while True:

  print("""              
              *** Menu ***
    [ 1 ] Cadastrar uma reserva
    [ 2 ] Entrada do cliente (check in)
    [ 3 ] Saída do cliete (check out)
    [ 4 ] Alterar reserva
    [ 5 ] Relatórios
    [ 6 ] Sair do programa
    
  """)

  opcao = int(input("Escolha uma das opções acima: "))

  if opcao == 1:
    funcaoCadastra()
  
  elif opcao == 2: 
    funcaoCheckIn()

  