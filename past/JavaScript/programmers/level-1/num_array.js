// https://programmers.co.kr/learn/courses/30/lessons/81301

// 숫자의 일부 자릿수를 영단어로 변경
// 14 = one4 등과 같은 문자열을 전부 숫자로 변경하면 됨

function solution(s) {
  const stringToNum = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  for (let i = 0; i < 10; i++) {
    s = s.split(stringToNum[i]).join(i);
  }
  return parseInt(s);
}

// best solution

function solution(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }

  return Number(answer); // Number가 parseInt보다 속도가 빠름
}
