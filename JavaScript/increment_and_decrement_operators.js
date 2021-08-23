let count = 1
const preIncrement = ++count
// 증감연산자를 앞에 놓게 되면 아래 주석으로 처리한 두 줄의 코드와 같은 내용입니다.
// 먼저 자기 자신에게 1을 더해서 재할당 한 후, 이를 preIncrement 에 할당했다는 의미입니다.
// count = count + 1
// const preIncrement = count
console.log(`count: ${count}, preIncrement: ${preIncrement}`) // count: 2, preIncrement: 2

let count2 = 1
const postIncrement2 = count2++
// 증감연산자를 뒤에 놓게 되면 아래 주석으로 처리한 두 줄의 코드와 같은 내용입니다.
// postIncrement에 자기 자신의 값을 먼저 할당하고, 이후에 1을 더해서 재할당합니다. 
// const postIncrement = count
// count = count + 1
console.log(`count: ${count2}, postIncrement: ${postIncrement2}`) // count2: 2, postIncrement2: 1