// https://programmers.co.kr/learn/courses/30/lessons/92334

// 게시판 불량 이용자 신고
// k번 신고가 쌓이면 해당 이용자를 신고한 이용자에게 처리 결과 메일 전송
// 한 이용자가 다른 이용자 한명을 여러 번 신고하면 1번으로 처리
// 자기 자신을 신고하는 경우는 없음

function solution(id_list, report, k) {
  var answer = [];
  const obj_id = {};
  const objReport = {};
  const banList = [];

  id_list.map((id) => (obj_id[id] = 0));

  const set = new Set(report);
  const newReport = [...set];

  const arrReport = newReport.map((rep) => rep.split(" "));

  arrReport.map((rep) => {
    if (!objReport[rep[1]]) {
      objReport[rep[1]] = 1;
    } else if (objReport[rep[1]]) {
      objReport[rep[1]] += 1;
    }
  });

  Object.keys(objReport).map((key) => {
    if (objReport[key] >= k) {
      banList.push(key);
    }
  });

  arrReport.map((rep) => {
    if (banList.includes(rep[1])) {
      obj_id[rep[0]] += 1;
    }
  });

  answer = Object.values(obj_id);
  return answer;
}

/// best solution

function solution(id_list, report, k) {
  let reports = [...new Set(report)].map((a) => {
    return a.split(" ");
  });
  let counts = new Map();
  for (const bad of reports) {
    counts.set(bad[1], counts.get(bad[1]) + 1 || 1);
  }
  let good = new Map();
  for (const report of reports) {
    if (counts.get(report[1]) >= k) {
      good.set(report[0], good.get(report[0]) + 1 || 1);
    }
  }
  let answer = id_list.map((a) => good.get(a) || 0);
  return answer;
}
