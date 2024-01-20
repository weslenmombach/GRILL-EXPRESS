import os

hamburguerias = [{'nome':'Alquimia Burguer', 'categoria':'Delivery', 'ativo':False}, 
                 {'nome':'Húmus & Hamburgers', 'categoria':'Local e delivery', 'ativo':True},
                 {'nome':'Kron Burguer', 'categoria':'Local e delivery', 'ativo':True}]

#No Python temos o os que é uma ferramenta que importa as funcionalidades do python no sistema operacional
#Para realizar uma função em Python, utilizamos o def
#No código foi usado bastente if, elif e else mas também pode ser usado o match que tem como utilidade realizar comparação, podendo definir padrões e casos
def exibir_nome_do_programa():
      print("""
      Ꮆ𝗚𝗥𝗜𝗟𝗟 𝗘𝗫𝗣𝗥𝗘𝗦𝗦\n""")

def exibir_funcoes():
      print('1 - Cadastrar Hamburgueria')
      print('2 - Listar Hamburguerias')
      print('3 - Alternar estado de Hamburgueria')
      print('4 - Sair\n')


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
      exibir_subtitulo('Encerrando o app\n')

def opcao_invalida():
      print('Opção Inválida!\n')
      voltar_ao_menu_principal()

def cadastrar_nova_hamburgueria():
    '''Essa função é responsável por cadastrar uma nova hamburgueria
    
    Inputs:
    - nome_da_hamburgueria
    - categoria_da_hamburgueria
    - estado_da_hamburgueria
    Outputs:
    - Adiciona uma nova hamburgueria a lista de hamburguerias
    '''
    #Utilização de lista, para uma coleção de dados;
    exibir_subtitulo('CADASTRANDO NOVA HAMBURGUERIA')
    nome_da_hamburgueria = input('Digite o nome da Hamburgueria: ')
    categoria_da_hamburgueria = input('Digite a categoria da Hamburgueria: ')
    estado_da_hamburgueria = input('A Hamburgueria está ativa? (Digite True ou False): ').lower() == 'true'

    nova_hamburgueria = {'nome': nome_da_hamburgueria, 'categoria': categoria_da_hamburgueria, 'ativo': estado_da_hamburgueria}
    hamburguerias.append(nova_hamburgueria)
    #append é pra adicionar algo na lista
    print(f'Hamburgueria {nome_da_hamburgueria} cadastrada com sucesso!')
    voltar_ao_menu_principal()



def listar_hamburguerias():

      exibir_subtitulo('LISTANDO HAMBURGUERIAS')
      print(f'{"NOME".ljust(22)} | {"CATEGORIA".ljust(20)} | STATUS')
      for hamburgueria in hamburguerias:
            nome_hamburgueria = hamburgueria['nome']
            categoria_hamburgueria = hamburgueria['categoria']
            ativo = 'Ativado' if hamburgueria['ativo'] else 'Desativado'
            print(f'- {nome_hamburgueria.ljust(20)} | {categoria_hamburgueria.ljust(20)} | {ativo.ljust(20)}')
      voltar_ao_menu_principal()

def alternar_hamburgueria():
      exibir_subtitulo('ALTERNANDO ESTADO DE HAMBURGUERIA')
      nome_hamburgueria = input('Digite o nome da Hamburgueria a ser alterada: ')
      hamburgueria_encontrada = False
      for hamburgueria in hamburguerias:
            if nome_hamburgueria == hamburgueria['nome']:
                  hamburgueria_encontrada = True
                  hamburgueria['ativo'] = not hamburgueria['ativo']
                  mensagem = f'A hamburgueria {nome_hamburgueria} foi ativada com sucesso!' if hamburgueria['ativo'] else f'A hamburgueria {nome_hamburgueria} foi desativada com sucesso!'
                  print(mensagem)
      if not hamburgueria_encontrada:
            print('A hamburgueria não foi encontrada')
      voltar_ao_menu_principal()


def escolher_opcao():
      try:
            opcao_escolhida = int(input('Digite uma opção: '))
            print(f'Você escolheu a opção {opcao_escolhida}.')
            
            if opcao_escolhida == 1:
                  cadastrar_nova_hamburgueria()
            elif opcao_escolhida == 2:    
                  listar_hamburguerias()
            elif opcao_escolhida == 3:
                  alternar_hamburgueria()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

#Abaixo temos a função main que determina que este é o arquivo/código principal do programa, fazendo com que seja executado esse arquivo
#Também é interessante para organizarmos e termos melhor visualização de chamadas de funções
def main():
      os.system('cls')
      #Utilizamos do os.system para zerar quando chamarmos o menu inicial novamente
      exibir_nome_do_programa()
      exibir_funcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()