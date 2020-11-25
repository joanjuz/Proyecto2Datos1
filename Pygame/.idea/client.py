import sys
import socket as sk

host = "127.0.0.1"
port = 2018

sCliente =  sk.socket()
sCliente.connect((host, port))
print("Conectado")

while True:
    inp = input("Texto para enviar: ")
    print("Enviar:", inp)
    salida = inp.encode("UTF8")
    print("Salida antes de enviar:", salida.decode("utf8"))
    lene = sCliente.send(salida)
    print("Se han enviado: {} bytes al servidor.".format(lene))
    ins = sCliente.recv(512)
    insd = ins.decode("UTF8")
    print("Servidor retorna:", insd)
    if inp == "exit":
        break

sCliente.close()
print("Terminado")