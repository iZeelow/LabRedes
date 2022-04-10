from asyncio.windows_events import NULL
from http import server
import socket
import socketserver

from numpy import void

def casos(numero):
    switcher = {
        0: [0,3,6],
        1: [0,4],
        2: [0,5,7],
        3: [1,3],
        4: [1,4,6,7],
        5: [1,5],
        6: [2,3,7],
        7: [2,4],
        8: [2,5,6]
    }
    return switcher.get(numero, "nothing")

def decision(array):
    player = [0,0,0,0,0,0,0,0]
    cpu = [0,0,0,0,0,0,0,0]
    contador = 0
    for elemento in array:
        if elemento == "X":
            temp = casos(contador)
            for x in temp:
                player[x] +=1
            contador+=1
        elif elemento =="O":
            temp = casos(contador)
            for x in temp:
                cpu[x] +=1
                contador+=1
    if contador >2:
        if 3 in player:
            return("player")
        if 3 in cpu:
            return("bot")
        else:
            return("empate")
    else:
        return
    



jugadas = [1,2,3,4,5,6,7,8,9]
UDP_IP = "localhost"
UDP_PORT = 5005

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
playersocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
playersocket.bind ("localhost" , 5001)
playersocket.listen(1)

conex, addr = playersocket.accept()
if conex.recv(1024).decode() == "anashe":
    #aki enviar la wea al gato revisar la conexion
    serversocket.sendto("anashe".encode(), (UDP_IP, UDP_PORT))
    mensajeudp, addr = serversocket.recvfrom(1024)
    mensajeudp = mensajeudp.decode
    if mensajeudp != NULL:
        mensajeudp = mensajeudp.split()
        UDP_IP = mensajeudp[0]
        UDP_PORT = mensajeudp[1]
        playersocket.send("anashe".encode())
        while True:
            jugada = conex.recv(1024).decode()
            jugadas[jugada] = "x"
            ganador = decision()
            if ganador == "player":
                playersocket.send("w")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            elif ganador == "bot":
                playersocket.send("l")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            elif ganador == "empate":
                playersocket.send("t")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            mensajeudp = "nosebroder"
            serversocket.sendto(mensajeudp.encode(), (UDP_IP, UDP_PORT))
            print("esperando mensaje del servidor")
            mensajeudp, addr = serversocket.recvfrom(1024)
            print("mensaje del servidor", mensamensajeudp.decode())
            jugadas[mensajeudp] =  'o'
            ganador = decision()
            if ganador == "player":
                playersocket.send("w")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            elif ganador == "bot":
                playersocket.send("l")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            elif ganador == "empate":
                playersocket.send("t")
                termino = playersocket.recv(1024).decode()
                if termino.decode() == "Terminar":
                    serversocket.sendto(termino, (UDP_IP,UDP_PORT))
                    break
            playersocket.send("continue".encode())
    else:
        mensajetcp = "GG"
        playersocket.send(mensajetcp)

