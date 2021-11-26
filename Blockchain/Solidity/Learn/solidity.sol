// 1. 컨트랙트 선언
contract Sample_a {
    // 2. 상태 변수 선언
    uint256 data;
    address owner;
    
    // 3. 이벤트 정의
    event logData(uint256 dataToLog);
    
    // 4. 함수 변경자 정의
    modifier onlyOwner() {
        if(msg.sender != owner) throw;
        _;
    }
    
    // 5. 생성자
    function Sample(uint256 initData, address initOwner) {
        data = initData;
        owner = initOwner;
    }
    
    // 6. 함수(메소드) 정의
    function getData() returns (uint256 returned) {
        return data;
    }
    function setData(uint256 newData) onlyOwner {
        logData(newData);
        data = newData;
    }
}

contract sample_b {
    // 동적 배열
    // 배열 리터럴이 보일 때마다 새로운 배열 생성
    // 배열 리터럴이 명시되어 있으면 스토리지에 저장되고, 함수 내부에서 발견되면 메모리에 저장된다.
    int[] myArray = [0, 0];
    function sample(uint index, int value) {
        myArray[index] = value;
        
        // myArray2는 myArray의 포인터를 저장!
        int[] myArray2 = myArray;
        // 메모리 내 고정된 크기의 배열
        uint24[3] memory myArray3 = [1, 2, 99999];
        // myArray4에 메모리에 있는 값을 스토리지에 할당할 수 없으므로 예외가 발생한다.
        // memory를 이용, 메모리에 할당해 주어야 에러가 없다.
        uint8[2] myArray4 = [1, 2];
    }
}

contract sample_c {
    // 문자열 리터럴이 있으므로 스토리지에 저장
    string myString = "";
    // 문자열 리터럴이 없어서 myRawString은 memory에 있다.
    bytes myRawString;
    
    function sample(string initString, bytes rawStringInit) {
        // 스토리지
        myString = initString;
        
        // myString2에 myString의 포인터를 저장
        string myString2 = myString
        
        // myString3은 메모리 내의 문자열
        string memory myString3 = "ABCDE";
        
        // 길이 및 내용 변경
        // myString3은 메모리에 위치해서 에러 X
        myString3 = "XYZ";
        myRawString = rawStringInit;
        
        // myRawString의 길이 증가
        myRawString.length++;
        
        // 메모리에 있는 "Example"을 스토리지의 myString에 저장하려 해서 에러 발생
        string myString4 = "Example";
        // 메모리에 있는 매개 변수(initString)을 스토리지의 myString5에 저장하려 해서 에러 발생
        string myString5 = initString;
    }
}