package main

import (
	"crypto/sha256"
	"fmt"
)

type block struct {
	data     string
	hash     string
	prevHash string
}

/*
Block 1
	b1Hash = (data + "x")

Block 2
	b2Hash = (data + b1Hash)

Block 3
	b3Hash = (data + b2Hash)


*/

func main() {
	/* get byte
	for _, aByte := range "Genesis Block" {
		fmt.Printf("%b\n", aByte)
	}
	*/

	genesisBlock := block{"Genesis Block", "", ""}
	hash := sha256.Sum256([]byte(genesisBlock.data + genesisBlock.prevHash))
	fmt.Println(hash)
	hexHash := fmt.Sprintf("%x", hash) // Sprintf -> 콘솔 출력없이 string return
	genesisBlock.hash = hexHash
	fmt.Println(genesisBlock)
}
