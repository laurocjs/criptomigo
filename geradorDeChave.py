from Crypto.PublicKey import RSA

# Gera a chave com 2048 bits
key = RSA.generate(2048)

privKey = key.exportKey()
pubKey =  key.publickey().exportKey()

privKeyObj = RSA.importKey(privKey)
pubKeyObj =  RSA.importKey(pubKey)

# Exporta a chave privada
handle = open('keys/chave_privada', 'w')
handle.write(privKey)
handle.close()

# Exporta a chave pública
handle = open('keys/chave_publica', 'w')
handle.write(pubKey)
handle.close()
