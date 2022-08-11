import Caver from "caver-js";
const caver = new Caver("https://public-node-api.klaytnapi.com/v1/cypress");

const bn = caver.getBlocknumber();

console.log(bn);
