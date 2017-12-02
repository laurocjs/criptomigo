# coding= utf-8
import random
from Crypto.PublicKey import RSA

# Função para sortear os pares
def sorteiaPares(listaDeParticipantes): # Recebe lista com nome dos participantes
                                        # e o valor é a chave pública dela
    dictSorteado = {}         # Dict a ser retornado
    numeroDeParticipantes = len(listaDeParticipantes) # Apenas para tornar o código mais limpo e legível

    if numeroDeParticipantes < 2:
        print "Você deve ter pelo menos dois participantes!!"
        return

    # Geramos então uma lista de N números aleatórios de 0 a N-1, sendo N o número de participantes
    # Para evitar problemas na distribuição, o primeiro número não pode ser 0
    # Caso seja, troco com algum outro número da lista
    sorteio = random.sample(xrange(numeroDeParticipantes), numeroDeParticipantes)
    if sorteio[0] == 0:
        rand = random.randint(1, numeroDeParticipantes-1)
        sorteio[0] = sorteio[rand]
        sorteio[rand] = 0

    # Realiza uma distribuição em que cada participante recebe outro participante aleatório
    iterator = 0
    for numero in sorteio:
        if iterator == numero: # A pessoa tirou ela própria
            # Nesse caso, ele troca com a pessoa anterior a ele na lista
            dictSorteado[listaDeParticipantes[iterator]] = dictSorteado[listaDeParticipantes[iterator-1]]
            dictSorteado[listaDeParticipantes[iterator-1]] = listaDeParticipantes[numero]
        else:
            dictSorteado[listaDeParticipantes[iterator]] = listaDeParticipantes[numero]
        iterator += 1

    return dictSorteado

# Função para criptografar o dict
def criptografaSorteio(dictDeChaves, dictSorteado): # Recebe dict Presenteante -> Chave e Presenteante -> Presenteado

    dictCriptografado = {}

    for participante in dictDeParticipantes:
        pubKeyObj = RSA.importKey(dictDeParticipantes[participante]) # Pega a chave pública do participante
        msg = dictSorteado[participante]    # Pega o presenteado sorteado para ele
        emsg = pubKeyObj.encrypt(msg, 'x')[0]   # Encripta o nome do sujeito
        caminho = "sorteio/" + participante
        with open(caminho, "w") as text_file:
            text_file.write(emsg)


# Início do programa:
# Crie a sua lista de participantes da maneira preferida
# A forma mais básica é:
listaDeParticipantes = [] # Uma lista de participantes
# Porém ler de um arquivo ou diretório também é interessante

dictDeParticipantes = {} # Um dict vazio
# Para cada participante, lê a sua chave e mapeia Participante -> Chave Pública
for participante in listaDeParticipantes:
    with open("chaves/pubKey" + participante, mode='r') as file:
        key = file.read()
        dictDeParticipantes[participante] = key

dictSorteado = sorteiaPares(listaDeParticipantes) # Recebe o dicionário que mapeia presenteante -> presenteado
criptografaSorteio(dictDeParticipantes, dictSorteado)
