package main

import "fmt"

func main() {
	name := "Wontae! ! ! ! Is my name"
	for _, letter := range name {
		fmt.Printf("%o", letter) // %b - binary | %d - digit | %x - hexadecimal
		// fmt.Println(letter)
		// fmt.Println(string(letter))
	}
}
