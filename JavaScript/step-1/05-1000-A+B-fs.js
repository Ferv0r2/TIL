// 백준 내 '/dev/stdin'에 테스트 파일 존재

const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin", "utf8").toString().split(" ");

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

console.log(A + B);
