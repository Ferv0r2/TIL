package main

import "fmt"

func main() {
	a := 2
	b := &a
	a = 12

	// 어떤 변수든 앞에 '&'를 붙이면 메모리 주소를 알 수 있음
	// 메모리 주소 값에 '*'를 붙이면 해당 값을 알 수 있음
	fmt.Println(*b)
}
