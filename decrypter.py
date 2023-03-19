import os
import pyaes

filename1 = "teste1.txt.ransomwaretroll"
filename2 = "teste1.xlsx.ransomwaretroll"

file1 = open(filename1,'rb')
file2 = open(filename2,'rb')

data = file1.read()
data2 = file2.read()

file1.close()
file2.close()
##  descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt1 = aes.decrypt(data)
decrypt2 = aes.decrypt(data2)

## remover o arquivo criptografado
os.remove(filename1)
os.remove(filename2)

## criar o arquivo descriptografado
new_file = "teste1.txt"
new_file2 = "teste1.xlsx"
new_file = open(f'{new_file}', "wb")
new_file2 = open(f'{new_file2}', "wb")
new_file.write(decrypt1)
new_file2.write(decrypt2)
new_file.close()
new_file2.close()