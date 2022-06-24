package person

import "fmt"

// export를 하기 위해서는 UpperCase 요구
type Person struct {
	name string
	age  int
}

func (p *Person) SetDetails(name string, age int) {
	p.name = name
	p.age = age
	fmt.Println("SetDetails' wontae:", p)
}

func (p Person) Name() string {
	return p.name
}

/* copy
func (p Person) SetDetails(name string, age int) {
	p.name = name
	p.age = age
	fmt.Println("SetDetails' wontae:", p)
}
*/
