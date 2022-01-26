import json
from textwrap import indent


def listar_discos(status):
    print('*********LISTA DE DISCOS************')
    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json') as b:
        data = json.load(b)

    for discos in data['discos']:
        if discos['status'] == status:
            numero = discos['numero']
            titulo = discos['titulo']
            cantor = discos['cantor']
            ano = discos['ano']
            print(numero, "-", titulo, ",", cantor, ",", ano)

def filtrar_discos(cantor):
    print('*********BUCA POR FILTRO************')
    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json') as b:
        data = json.load(b)

    print('lista dos discos de:', cantor)

    for discos in data['discos']:
        if discos['cantor'] == cantor:
            titulo = discos['titulo']
            ano = discos['ano']
            print(titulo,ano)



def emprestar_disco(numero_emprestar, emprestado_para):
    numero_emprestar = numero_emprestar
    emprestado_para = emprestado_para
    status_Indisponivel = 'indisponivel'

    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json') as b:
        data = json.load(b)

    for disco in data['discos']:
        if disco['id'] == numero_emprestar:
            disco['status'] = status_Indisponivel
            disco['emprestado_para'] = emprestado_para
            print('disco ', disco['id'], disco['titulo'], 'emprestado para ', emprestado_para)

    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json', 'w') as b:
        json.dump(data, b)


def devolver_disco(id):
    status_disponivel = 'Disponivel'

    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json') as b:
        data = json.load(b)

    for disco in data['discos']:
        if disco['id'] == id:
            disco['status'] = status_disponivel
            disco['emprestado_para'] = ""

    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json', 'w') as b:
        json.dump(data, b)


def doar_disco(id, numero, titulo, cantor, ano):
    new_disco = {
        'id': id,
        'numero': numero,
        'titulo': titulo,
        'ano': ano,
        'cantor': cantor,
        'emprestado_para': " ",
        'status': 'disponivel'
    }

    with open('C:/Users/SAFIRA/PycharmProjects/castrado_discos/db/discos.json', "r+") as file:
        file_data = json.load(file)
        file_data['discos'].append(new_disco)
        file.seek(0)
        json.dump(file_data, file, indent = id)


if __name__ == '__main__':
   # listar_discos()
   # emprestar_disco(1, 'sofia')
   # devolver_disco(1)
   print('#############################')
   print('#     MENU DE OPÇÕES        #')
   print('#                           #')
   print('# 1 - Listar Discos         #')
   print('# 2 - Emprestar Discos      #')
   print('# 3 - Devolver Discos       #')
   print('# 4 - Doar Discos           #')
   print('# 5 - Busca por filtro      #')
   print('#                           #')
   print('# 9 - Sair                  #')

   resposta = input('escola sua opção:      ')
   print(f'A sua escolha foi:     {resposta}')

   if resposta.upper() != '9':
      if resposta == '1':
         listar_discos("Disponivel")
      elif resposta == '2':
           numero_do_disco = input('digite o codigo do livro:   ')
           pessoa = input('digite o nome da pessoa que ficara com disco:  ')
           emprestar_disco(int(numero_do_disco), pessoa)
      elif resposta == '3':
           id = input('digite o id do disco:  ')
           devolver_disco(int(id))
      elif resposta == '4':
          id = input('digite o id do disco:     ')
          print ('Você escolheu a opção doar disco')
          numero = input('digite o numero do disco: ')
          titulo = input('digite o nome titulo do disco: ')
          cantor = input('digite o nome do cantor do disco: ')
          ano = input('digite o ano do disco: ')
          doar_disco(int(id),numero, titulo, cantor, ano)
      elif resposta == '5':
         cantor = input('Digite o cantor para pesquisar:')
         filtrar_discos(cantor)
      else:
         print('Você digitou uma opçao invalida. Escola uma opcao de 1 a 4')
else:
     print('Voce escolheu sair. Obrigada')
