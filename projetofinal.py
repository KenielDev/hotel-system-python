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

  banco.writelines("{},{},{},{},{},{},{},".format(insereCliente,insereCpf,numeroPessoas,tipoQuarto,numeroDias,valor,status[0]) + "\n")
  
  banco.close()
  
  print("Cadastro concluído com sucessso!")

def funcaoBusca():
    arquivo = open("database.txt", "r")
    listaClientes = arquivo.readlines()
    arquivo.close

    novaLista = []
    for i in listaClientes:
        insereCliente,insereCpf,nPessoas,tipoQuarto,valor,nDias,status,nothing = i.split(",")
        clientes = {"nome" : insereCliente, "cpf" : insereCpf, "nPessoas" : nPessoas, "tipoQuarto" : tipoQuarto, "nDias" : nDias, "valor" : valor, "status" : status}
        novaLista.append(clientes)
    return novaLista


def funcaoAltera(novaLista):
    arquivo = open("database.txt", "w")
    for i in novaLista:
        arquivo.write(f"{i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
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
            print(f"Reserva n°:{reserva} - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                i['status'] = "A"
    funcaoAltera(novaLista)
    
    print("Check in realizado com sucesso!!")


def funcaoCheckOut():
    cpf = input("Procurar por cpf: ")
    
    novaLista = funcaoBusca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                i['status'] = "F"
    funcaoAltera(novaLista)
    
    print("Check out realizado com sucesso!!")

def funcaoAlterarReserva():
    cpf = input("Procurar por cpf: ")
    
    novaLista = funcaoBusca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                    i['nPessoas'] = int(input("Numero de pessoas: "))
                    i['nDias'] = int(input("Numero de dias: "))
                    i['tipoQuarto'] = input("Tipo de quarto (<S>Standar <D>Delux <P>Premium): ").upper()
                    i['status'] = input("Status do quarto: ").upper()
                    if(i['tipoQuarto'] == "S"): i['valor'] = (100*i['nPessoas'])*i['nDias']
                    elif(i['tipoQuarto'] == "D"): i['valor'] = (100*i['nPessoas'])*i['nDias']
                    elif(i['tipoQuarto'] == "P"): i['valor'] = (100*i['nPessoas'])*i['nDias']
    funcaoAltera(novaLista)
    
    print("Alteração realizada com sucesso!!")

def relatorio():
    
    novaLista = funcaoBusca()
    cho = int(input("1 - Relatório de todas as reservas com status R\n2 - Relatório de todas as reservas com status C\n3 - Relatório de todas as reservas com status A\n4 - Relatório de todas as reservas com status F\n5 - Relatório total recebido\n6 – Relatório de Reserva por pessoa\n> "))
    if cho == 1:
        reserva = 0
        for i in novaLista:
            if("R" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    elif cho == 2: 
        reserva = 0
        for i in novaLista:
            if("C" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    elif cho == 3: 
        
        reserva = 0
        for i in novaLista:
            if("A" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    elif cho == 4: 
        
        reserva = 0
        for i in novaLista:
            if("F" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")
    elif cho == 5: 
        
        totalRecebido=0
        for i in novaLista:
            totalRecebido+=int(i["valor"])
        print(f"Total Recebido = {totalRecebido}")
    elif cho == 6: 
        cpf = input("Procurar por cpf: ")
        
        reserva = 0
        for i in novaLista:
            if(cpf == i['cpf']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['nDias']},{i['valor']},{i['status']},\n")

    
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

  elif opcao == 3:
    funcaoCheckOut()  

  elif opcao == 4:
    funcaoAlterarReserva()