# BLOCKCHAIN TECHNOLOGY


## BLOCKCHAIN
    : Cryptocurrency ( crypto:암호화 | currency:화폐 )

- 2009년 비트코인이 처음 세상에 등장했을 때, 비트코인의 성격을 규정하는 용어
- 한국에서는 '암호화폐'라 칭함

---

* Blockchain = Chain + Block

1. Append : Append만 가능한 Database

2. Decentralization (탈중앙화) : 모두가 동일한 DB 복제본 소유

---

* Block = Data + Hash

1. 비트코인의 경우 Data = Transaction (거래내역)

2. Hash = 일방향 함수 (Input -> Output만 가능, 반대는 불가), 결정론적

---

* Block에 참여하기 위한 방법

Hash(Transaction 수집 + 이전 블록의 Hash 수집)

---

* Proof of work ( 작업증명 )

네트워크를 거짓 정보로 부터 보호

- Mining

A. 거래내역을 확인 -> 데이터를 블록에 삽입 -> 블록체인에 추가

A 과정을 통해 일종의 수수료를 지급

B. 네트워크에서 질문을 제공 -> 해당 질문의 답을 찾아 블록을 체인에 업로드

B 과정을 통해 블록 생성 시, coinbase transaction 발생 (비트코인 생성)

! 최초 50개씩 발행되었으나 현재는 6.25개씩 발행

=> 비트코인의 생산량이 한정되어 있기 때문 ( 2100만 개 )

- B 과정 소개

Difficulty : ex) Hash 값 Output에서 앞에 오는 0의 개수 (비트코인은 Bits를 사용)

Nonce : Miner가 바꿀 수 있는 유일한 값

Nonce를 변경할 시, Hash 값 변경 -> Difficulty에 걸맞는 값 찾기

=> 그래픽카드는 Nonce 값을 굉장히 빠르게 연산 가능



## Smart Contract

주인이 없는 Database에 아무도 수정할 수 없는 계약 업로드

중개인 없이 네트워크를 이용한 거래가 가능함

Limitatoins -> 원하는 소스를 다 활용할 수 없음

해당 블록체인 네트워크에서만 사용 가능 ( 의존성 )

신뢰 기반이 아닌 특수한 네트워크 환경 요구

방안 -> Oracle이 Smart Contract에 Input 제공



## Non Fungible Token

원본임을 증명할 수 있는 기술

NFT를 통한 소유권, 원본 증명, 창작자 확인 등이 가능



## Wallet

집문서에서 집주인을 바꾸듯이 비트코인을 직접 네트워크에서 거래하는 것 아닌
기존 주인의 지갑 주소에서 나의 지갑 주소로 변경하는 개념

- 비대칭 암호

각각 Public Key, Private Key가 존재

Public Key -> 자물쇠, Private Key -> 키



## DeFi

탈중앙화된 금융

Stable Coin = TETHER, USDC, BUSD

AVVE -> 오직 Smart Contract로 거래

- 유동성 풀

A 코인을 받으면 B 코인을 주는 Smart Contract

돈을 예치하는 순간 타인은 해당 금액을 빌리면서 수수료를 제공

오직 Code로만 구성



# Darkside of Bitcoin

* Slow & InEfficient

- 단 1 개의 비트코인 거래를 위해 필요한 에너지는 
한 달 동안 한 가구가 쓰는 에너지 용량과 맞먹음

=> 중국이 작업증명의 절반을 차지 -> 작업 증명을 하기 위해 전기가 필요 
-> 석탄 발전소 등을 운영하면서 환경 오염 ( 태양열로 하면 해결되나 현재 그렇지 못함 )

같은 에너지량이면 Visa 네트워크는 60만 거래를 처리 가능

- 전체 비트코인 네트워크가 1년간 사용하는 에너지 총량은 
체코의 국가 총 에너지 사용량과 맞먹음

- 개인정보 보호 X

1. Government Regulation

- 정부가 거래소를 통제

- aka KimChi Premium

2. Scam

- 해당 프로젝트가 망했을 때, 개발자가 도망갔을 때 
아무도 도와줄 수 없음

- 즉, 자신이 공부하고 구분해야 함

3. Technical Challenges

- 1G | Bitcoin

오직 전송, 업데이트 불가능 (금과 같은 개념)

- 2G | Ethereum

Smart Contract 적용. 전세계가 공유하는 컴퓨터

프로그래밍 할 수 있는, 해킹할 수 없는

(현재 이더리움도 3G 전환을 진행중)

! 과도한 트래픽으로 인한 거래 수수료 상승

! 블록체인간 호환 및 통신 불가

! Solidity를 배워야 함

- 3G | Solana, Algorand, Cardano

트릴레마의 3요소를 만족시키는 코인(Scalable, Decentralized, Secure)



## Consensus PoW

해당 블록 추가에 대해 Agree or Disagree

* 51% Attack

전체 네트워크의 51%를 차지하여 거짓 정보여도 Agree

* Hard Forks

채굴자들 사이에 합의가 되지 않을 경우 발생

이를 통해 블록체인이 업데이트



## Proof of Stake | 3G

네트워크에서 받는 보상의 양은 보유한 코인양과 보유한 시간에 비례

! 부자가 더 부자가 되는 시스템

! 얼리 어답터에게 유리



# Delegated Proof of Stake

누구나 검증자가 될 수 있음

선거를 해서 대선 승부를 하듯 진행

위임자에게 맡기고 위임자가 보상을 나누는 식



