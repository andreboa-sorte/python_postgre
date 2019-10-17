from operacao_banco import Operacoes

op = Operacoes()

menu=True
while menu:
    aux=int(input("1- cadastrar\n"
                  "2- atualizar\n"
                  "3- listar\n"
                  "4- deletar\n"
                  "5- sair\n"
                  "opção: "))

    if aux==1:

        nome = str(input("Digite o nome da pessoa: "))
        sobrenome = str(input("Digite o sobrenome de {0}: ".format(nome)))
        curso=str(input("digite o curso de {0}: ".format(nome)))
        op.salvar(nome,sobrenome,curso)

    elif aux==2:

        id=int(input("digite o o ID do cadastro a ser atualizado: "))

        nome=str(input("digite novo nome: "))
        sobrenome=str(input("digite o novo sobrenome: "))
        curso=str(input("digite o novo curso: "))

        op.atualizar(id,nome,sobrenome,curso)


    elif aux == 3:
        op.listar()

    elif aux==4:
        id=int(input("digite o ID do registro a ser deletado: "))
        op.deletar(id)

    elif aux==5:
        menu=False
