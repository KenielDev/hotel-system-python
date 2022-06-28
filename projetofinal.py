
#Alerta caso o campo esteja vazio
from gettext import find


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

  inserteCpf = input("Insira o cpf do titular: ")
  validaCpf = len(inserteCpf)
  while (validaCpf < 11):
    print("\033[0;31mCampo incorreto!\033[m")
    tipoQuarto = input("Por favor digite o CPF corretamente: ")
  
  numeroPessoas = input("Insira o número de pessoas: ")
  funcaoAlert(numeroPessoas)

  tipoQuarto = input("Insira o tipo do quarto: ")
  while((tipoQuarto != "S") and (tipoQuarto != "s") and (tipoQuarto != "D") and (tipoQuarto != "d") and (tipoQuarto != "P") and (tipoQuarto != "p")):
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

  banco.writelines("Nome: {}; CPF: {}; Número de pessoas hospedadas: {}; Tipo de quarto: {}; Dias de hospedagem: {}; Valor total: {}; Status: {}".format(insereCliente,inserteCpf,numeroPessoas,tipoQuarto,numeroDias,valor,status[0]) + "\n")
  
  banco.close()
  
  print("Cadastro concluído com sucessso!")

def funcaoCheckIn():
  with open("database.txt", "w") as clientes:

    cpf = input("Digite o cpf do cabra: ")

    for cpf in clientes:

      altera = cpf.writelines()

      return altera

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

  