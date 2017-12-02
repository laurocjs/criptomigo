from Crypto.PublicKey import RSA

# Digite seu nome abaixo
nome = "BillGates"

# Abre a chave
with open("keys/chave_privada" + nome, mode='r') as file:
    key = file.read()

# Abre a mensagem do sorteio
with open("sorteio/" + nome, mode='r') as file:
    emsg = file.read()

privKeyObj = RSA.importKey(key)

dmsg = privKeyObj.decrypt(emsg)
print "O amigo sorteado para você foi: " + dmsg
