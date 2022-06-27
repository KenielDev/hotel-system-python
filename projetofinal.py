
banco = open("database.txt", "a")

def funcaoCadastra():

  clientes = list()

  insereCliente = input("Insira o nome do titular: ")

  while(insereCliente == ""):
    print("\033[0;31mEste é um campo obrigatório!\033[m")
    print(insereCliente)
   
  inserteCpf = input("Insira o cpf do titular: ")
  numeroPessoas = input("Insira o número de pessoas: ")
  tipoQuarto = input("Insira o tipo do quarto: ")
  numeroDias = input("Insira o numero de dias da reserva: ")

  nPessoas = int(numeroPessoas)
  nDias = int(numeroDias)

  #calcula o valor total da diaria

  if tipoQuarto == "S":
    valorQuarto = 100

  elif tipoQuarto == "D":
    valorQuarto = 200

  elif tipoQuarto == "P":
    valorQuarto = 300


  #calcula o valor total da diaria

  valor = nPessoas * nDias * valorQuarto

  #insere o cadastro no banco
  status = input("Insira o status do titular: ")

  banco.writelines("Nome: {}; CPF: {}; Número de pessoas hospedadas: {}; Tipo de quarto: {}; Dias de hospedagem: {}; Valor total: {}; Status: {}".format(insereCliente,inserteCpf,numeroPessoas,tipoQuarto,numeroDias,valor,status) + "\n")
  
  banco.close()

  


while True:

  print("""              *** Menu ***
  [ 1 ] Cadastrar uma reserva
  [ 2 ] Entrada do cliente (check in)
  [ 3 ] Saída do cliete (check out)
  [ 4 ] Alterar reserva
  [ 5 ] Relatórios
  [ 6 ] Sair do programa""")

  opcao = int(input("Escolha uma das opções acima: "))

  if opcao == 1:
    funcaoCadastra()