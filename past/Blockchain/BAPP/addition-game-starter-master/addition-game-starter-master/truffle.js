// truffle.js config for klaytn.
const PrivateKeyConnector = require('connect-privkey-to-provider')
const NETWORK_ID = '1001'
const GASLIMIT = '20000000'
const URL = 'https://api.baobab.klaytn.net:8651'
const PRIVATE_KEY = '0x0d124aeece1666b0d0a0ffb33a3dce5da085f1cbf958b06a2ec5fec77a4e71b0'

module.exports = {
    networks: {
        klaytn: {
            provider: new PrivateKeyConnector(PRIVATE_KEY, URL),
            newwork_id: NETWORK_ID,
            gas: GASLIMIT,
            gasPrice: null
        }
    }
}