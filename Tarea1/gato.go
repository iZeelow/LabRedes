package main

import (
	"fmt"
	"net"
	"math/rand"
	"time"
)

func main() {

	rand.Seed(time.Now().Unix())
	min := 0
	max := 8
	random := fmt.rand.Intn((max - min) + min)
	minport := 8000
	maxport := 65535
	PORT := ":5000"
	BUFFER := 1024
	s, err := net.ResolveUDPAddr("udp4", PORT)

	if err != nil {
		fmt.Println(err)
		return
	}

	connection, err := net.ListenUDP("udp4", s)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer connection.Close()


	buffer := make([]byte, BUFFER)

	fmt.Println("esperando mensaje del servidor intermedio")
	n, addr, _ := connection.ReadFromUDP(buffer)
	msg := string(buffer[:n])

	if msg == "algunawea"{
		randomport := fmt.rand.Intn((maxport - minport) + minport)
		info := (ip,randomport)
		//abrir la conexion aca en el puerto random 
		_,_ = connection.WriteToUDP(info, addr)
	}

	fmt.Println("direccion:", addr)
	fmt.Println("mensaje del servidor intermedio:", msg)
	response := []byte("adios")
	_, _ = connection.WriteToUDP(response, addr)
	return
}
