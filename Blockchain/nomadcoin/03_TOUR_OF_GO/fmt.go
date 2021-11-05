package main

import "fmt"

func main() {
	x := 405940594059
	xAsBinary := fmt.Sprintf("%b\n", x)
	fmt.Println(x, xAsBinary)
	// fmt.Printf("%o\n", x)
	// fmt.Printf("%x\n", x)
	// fmt.Printf("%U\n", x)
}
