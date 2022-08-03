function solution(n, k) {
  const result = [];
  let arr = Array.from(new Array(n), (x, i) => i + 1);
  let fac = arr.reduce((acc, val) => acc * val, 1);
  k--;

  while (result.length !== n) {
    fac = fac / arr.length;
    let tmp = arr[Math.floor(k / fac)];
    result.push(tmp);
    k = k % fac;
    arr = arr.filter((e) => e !== tmp);
    console.log(fac, tmp, result, k, arr);
  }

  return result;
}
