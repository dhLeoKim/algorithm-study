## 백준 파일 제출 폼

### input 입력받기
* FileInputStream
* Scanner
* nextInt()
* next()

```java
import java.io.FileInputStream;                                     // 입력 - 제출시 지우기
import java.io.IOException;                                         // 입력
import java.util.Scanner;                                           // 입력

// 제출시 클래스명 Main으로 수정
public class boj11720 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11720.txt"));     // txt 파일 읽어오기 - 제출시 지우기
        Scanner sc = new Scanner(System.in);                        // Scanner로 입력 받기
        int N = sc.nextInt();                                       // nextInt()로 정수 입력받기
        String sNum = sc.next();                                    // next()로 문자열 입력 받기
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for(int i = 0; i < cNum.length; i++) {
//            sum += cNum[i] - '0';
            sum += Character.getNumericValue(cNum[i]);
        }

        System.out.println(sum);
    }
}

```

### 데이터 타입(문자열, 정수)
* toCharArray()

#### char -> int
1. 아스키코드 이용
```java
int num = '1' - '0'; //  49(문자열 '1' 아스키값) - 48(문자열 '0' 아스키값) 
```
2. getNumericValue
```java
char cNum = '1';
int num = Character.getNumericValue(cNum);
```

### string -> int
```java
String str = "25";
int num = Integer.parseInt(str);
```

### 자동형변환
```java
// sum, max, N 모두 int 이지만
// 100.0을 곱해 double로 자동 형변환
System.out.println(sum*100.0/max/N);
```

### input 입력받기 2
* FileInputStream
* BufferedReader
    * 예외 처리 필수
    * try catch 문 또는 IOException 사용
    * String으로 입력 받기에 필요에 따라 형변환
* StringTokenizer
    * StringTokenizer("문자열", "구분자", true/false)
    * 구분자로 분할하여 토큰화
    * 구분자 옵션 안쓰면 디폴트는 띄어쓰기로 분할
    * true/false로 구분자도 token취급 가능, 디폴트는 false
    * .nextToken()
    * 으로 하나의 토큰 사용
```java
// 입력
// 5 3

        System.setIn(new FileInputStream("./input_11659.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());       // 한 줄을 문자열로 입력받기 : 5 3
        int N = Integer.parseInt(stringTokenizer.nextToken());                                  // 첫번째 : 5
        int M = Integer.parseInt(stringTokenizer.nextToken());                                  // 두번째 : 3
```
#### StringTokenizer vs Split
* StringTokenizer는 클래스
* StringTokenizer는 문자/문자열로 구분
* StringTokenizer결과는 문자열
* StringTokenizer는 빈 문자열을 토큰으로 인식x
* 
* Split은 String의 메서드
* Split은 정규표현식
* Split결과는 문자열 배열
* Split은 빈 문자열을 토큰으로 인식

#### BufferedReader vs Scanner
* 백준에서 input 입력시의 속도차이 발생
    * BufferedReader가 더 빠름
* BufferedReader
    * 입력받은 값을 8192char (16384 byte) 크기의 버퍼에 담아두었다가 한번에 전송
* Scanner
    * 입력즉시 전송, 정수, 소수, 문자 구분해서 입력

