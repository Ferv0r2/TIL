// https://programmers.co.kr/learn/courses/30/lessons/72410

// 아이디 길이는 3 이상 15 이하
// 아이디는 소문자, 숫자, -, _, . 만 가능
// .는 처음과 끝에 사용할 수 없으며 연속도 안됨

// 아래와 같은 절차로 처리
// 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
// 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
// 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
// 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
// 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
// 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
//      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
// 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

function solution(new_id) {
  let answer = new_id
    .toLowerCase() //step 1
    .replace(/[^0-9a-z._-]/g, "") // step 2
    .replace(/\.+/g, ".") //step 3
    .replace(/^\.|\.$/g, "") //step 4
    .replace(/^$/, "a") //step 5
    .slice(0, 15)
    .replace(/\.$/, ""); //step 6
  // step7
  if (answer.length === 1) answer = answer[0].repeat(3);
  if (answer.length === 2) answer = answer + answer[1];

  return answer;
}

// best solution

function solution(new_id) {
  const answer = new_id
    .toLowerCase() // 1
    .replace(/[^\w-_.]/g, "") // 2
    .replace(/\.+/g, ".") // 3
    .replace(/^\.|\.$/g, "") // 4
    .replace(/^$/, "a") // 5
    .slice(0, 15)
    .replace(/\.$/, ""); // 6
  return answer.padEnd(3, id[id.length - 1]);
}
