package main

import "fmt"

func main() {
	// foods := [3]string{"potato", "pizza", "pasta"} // array
	foods := []string{"potato", "pizza", "pasta"} // slice
	fmt.Printf("%v\n", foods)
	fmt.Println(len(foods))
	foods = append(foods, "tomato")
	fmt.Printf("%v\n", foods)
	fmt.Println(len(foods))
	/* array
	for _, food := range foods {
		fmt.Println(food)
	}
	for i := 0; i < len(foods); i++ {
		fmt.Println(foods[i])
	}
	*/
}

// slice = list
