package main

import "fmt"

type person struct {
	name string
	age  int
}

// func (변수명 Struct) receiver() {}
func (p person) sayHello() {
	fmt.Printf("Hello! My name is %s and I'm %d", p.name, p.age)
}

func main() {
	// 순서 상관X, label 선택O
	wontae := person{"wontae", 24}
	// nico := person{name: "nico", age: 29}
	// minsu := person{age: 15, name: "minsu"}

	wontae.sayHello()
}

// Go language's structs = class
// Go language's receiver = method
