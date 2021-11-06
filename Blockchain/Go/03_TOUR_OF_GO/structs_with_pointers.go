package main

import (
	"fmt"
	"person" // Go/src/person
)

func main() {
	wontae := person.Person{}
	wontae.SetDetails("wontae", 24)
	fmt.Println("Main's wontae", wontae)
}
