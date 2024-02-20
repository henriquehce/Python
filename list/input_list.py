def escolhercor():
    cores = ['verde', 'amarelo', 'azul', 'vermelho', 'pretoebranco', 'lilaz']

    while True:
        cor_cliente = input('Digite a cor desejada (ou digite 0 para sair): ').strip()

        if cor_cliente == '0':
            break
        elif cor_cliente.lower() in cores:
            print("Disponível")
        else:
            print('Não disponível')

escolhercor()
