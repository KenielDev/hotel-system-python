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

def funcaoCheckIn():
  with open("database.txt", "r") as banco:

    lista = banco.read()

    status = "R"
    newStatus = "A"

    lista = lista.replace(status, newStatus)

  with open('database.txt', 'w') as banco:
  
    banco.write(lista)
    
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

  