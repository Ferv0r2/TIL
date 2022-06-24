// https://programmers.co.kr/learn/courses/30/lessons/77484

// 로또, 1 ~ 45 숫자 중에서 6개를 찍어서 맞추는 것
// 낙서로 알아볼 수 없는 번호는 0으로 처리
// 만약 0으로 처리된 것이 맞다면, 최고 순위
// 전부 틀리다면 최저 순위
// 모두 맞으면(6개) 1등, 모두 틀리면(0개) 6등

function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];

  const zeroCount = lottos.filter((e) => e === 0).length;
  const matchCount = win_nums.filter((e) => lottos.includes(e)).length;

  const lowRank = rank[matchCount];
  const highRank = zeroCount === 6 ? 1 : rank[matchCount + zeroCount];

  return [highRank, lowRank];
}

/// best solution

function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];

  let minCount = lottos.filter((v) => win_nums.includes(v)).length;
  let zeroCount = lottos.filter((v) => !v).length;

  const maxCount = minCount + zeroCount;

  return [rank[maxCount], rank[minCount]];
}
