// 인터페이스 선언 필요, close가 없으면 NaN값 에러 발생

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input = line.split(" ").map((el) => parseInt(el));
  rl.close();
});

rl.on("close", () => {
  let a = input[0];
  let b = input[1];
  console.log(a + b);
});
