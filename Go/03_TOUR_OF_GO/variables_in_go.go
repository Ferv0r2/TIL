package main

// var name string = "wontae"
const name string = "nico"

func plus(a ...int) int {
	var total int // total := 0
	for _, item := range a {
		total += item
	}
	return total
}

// func main() {
// 	result := plus(2, 3, 4, 5, 6, 7, 8, 9, 10)
// 	fmt.Println(result)
// }


// func plus(a, b int, name string) (int, string) {
// 	return a + b, name
// }


// func main() {
// 	var name string = "wontae"
// 	name := "wontae" // 함수 밖에서는 사용 X :=
// 	age := 12
// 	result, name := plus(2, 2, "nico")
// 	fmt.Print(result, name)
// }

// int 양수 음수 모두 가능
// uint 양수만 가능
