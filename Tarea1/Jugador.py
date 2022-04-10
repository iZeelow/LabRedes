import socket

def slot(argument):
    switcher = {
        "0,0": 0,
        "0,1": 1,
        "0,2": 2,
        "1,0": 3,
        "1,1": 4,
        "1,2": 5,
        "2,0": 6,
        "2,0": 7,
        "2,0": 8
    }
    return switcher.get(argument, "nothing")

print("-----------Benvenido a juego de seu mama---------------\n")
print("- Seleccione una opción\n")
print("1-Jugar\n")
print("2-Salir\n")
arr = [" "," "," "," "," "," "," "," "," "]
tablero = ". 0 | 1 | 2\n 0 {}| {} |{}\n ---+---+--- \n 1 {}| {} |{} \n ---+---+--- \n 2 {}| {} |{} \n".format(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8])
choice = input()
if choice == "1":
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost",5001))
        s.send("anashe".encode())
        resp = s.recv(1024).decode()
        if resp == "anashe":
            juego = True
            break
        else:
            print("Ha habido un error, presione 1 para iniciar el juego")
            temp = input()
            if temp == "1":
                continue
            else:
                exit()
    print("--------Comienza el Juego--------")
elif choice == "2":
    exit() 
while juego:
    print(tablero)
    jugada = input("Ingrese su jugada (x,y)")
    pos = slot(jugada)
    arr[pos] = "x"
    s.send(pos.encode())
    resp = s.recv(1024).decode()
    if resp == "continue":
        continue
    elif resp == "w":
        print("Ganaste")
        s.send("Terminar".encode())
        break
    elif resp == "l":
        print("Perdiste")
        s.send("Terminar".encode())
        break
    elif resp == "t":
        print("Empate")
        s.send("Terminar".encode())
        break