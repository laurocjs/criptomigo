# criptomigo
Sistema de amigo oculto utilizando criptografia RSA

Leia o arquivo LICENCA.txt.
Os arquivos contidos aqui servem para realizar um sorteio utilizando chaves públicas e privadas RSA.

Utilização:
Para gerar uma dupla de chaves privada/pública, execute o arquivo geradorDeChave.py
(ex.: $ python geradorDeChave.py)
A saída estará na pasta keys.

Para gerar um sorteio, execute o arquivo sorteio.py. Ele irá procurar as chaves públicas
dos participantes no caminho ./chaves/ pelo nome pubKey[NomeDoParticipante].
(ex.: $ python sorteio.py)

O resultado do sorteio estará na pasta sorteio. O nome do arquivo indica quem deve
receber a mensagem indicada, ou seja, o presenteante é o nome do arquivo e o presenteado
é o conteúdo do arquivo (criptogrado).

Para ler quem foi o sorteado, basta utilizar o arquivo leitorDeAmigo.py. É necessário
editar o arquivo para incluir o seu nome (ou de quem quer ler a mensagem). Ele utiliza
o arquivo keys/chave_privada para efetuar a desencriptação do arquivo sorteio/[SeuNome]
e imprime no console o resultado no console.
(ex.: $ python leitorDeAmigo.py)
