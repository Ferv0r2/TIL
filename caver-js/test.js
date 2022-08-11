const Caver = require("caver-js");
const caver = new Caver("https://public-node-api.klaytnapi.com/v1/cypress");

const getBN = async () => {
  const bn = await caver.klay.getBlockNumber();
  console.log(bn);
};

getBN();
