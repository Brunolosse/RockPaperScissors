from random import randint

ppt = {1:'Pedra',2:'Papel',3:'Tesoura'}
opcao =''
vjogador = 0
vmaquina = 0
empates = 0
rodadas = 0

while True:
    opcao = input('Escolha 1. Pedra, 2. Papel, 3. Tesoura ou 4. Para sair: ')
    if opcao == '4':
        break
    try:
        opcao = int(opcao)
        if opcao not in ppt:
            raise ValueError('Opção inválida')
    except ValueError:
        print('Você entrou com um valor incorreto')

        continue

    ejogador = ppt[opcao]
    maquina = ppt[randint(1, 3)]

    print(f'A máquina jogou {maquina}')

    if ejogador == 'Pedra' and maquina == 'Tesoura':
        print('Jogador venceu esta rodada!')
        vjogador += 1
    if ejogador == 'Papel' and maquina == 'Pedra':
        print('Jogador venceu essa rodada!')
        vjogador += 1
    if ejogador == 'Tesoura' and maquina == 'Papel':
        print('Jogador venceu essa rodada!')
        vjogador += 1

    if maquina == 'Pedra' and ejogador == 'Tesoura':
        print('A máquina venceu esta rodada!')
        vmaquina += 1
    if maquina == 'Papel' and ejogador == 'Pedra':
        print('A máquina venceu essa rodada!')
        vmaquina += 1
    if maquina == 'Tesoura' and ejogador == 'Papel':
        print('A máquina venceu essa rodada!')
        vmaquina += 1

    if maquina == 'Pedra' and ejogador == 'Pedra':
        print('Essa rodada terminou em empate!')
        empates += 1
    if maquina == 'Papel' and ejogador == 'Papel':
        print('Essa rodada terminou em empate!')
        empates += 1
    if maquina == 'Tesoura' and ejogador == 'Tesoura':
        print('Essa rodada terminou em empate!')
        empates += 1
    rodadas += 1

if vjogador > vmaquina:
    print('\nO jogador venceu!!!!\n')
elif vmaquina > vjogador:
    print('\nA máquina venceu :(\n')
else:
    print('\nO jogo terminou em empate\n')


print(f'Vitorias do jogador: {vjogador}')
print(f'Vitórias da máquina: {vmaquina}')
print(f'Total de empates: {empates}')
print(f'Total de rodadas jogadas: {rodadas}')






