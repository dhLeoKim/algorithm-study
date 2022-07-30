# week1 : Big-O , sort , 수학
## Big-O
* 알고리즘의 성능을 수학적으로 표기
  
* 시간복잡도, 공간복잡도를 표현 가능
  
* 알고리즘의 실제 러닝타임을 표기하는것이라기 보다,
  
* 데이터나 사용자의 증가율에 따른 알고리즘의 성능을 예측하는 것이 목표

* 따라서 알고리즘의 성능을 점근적 표기하기에 상수는 취급x
  * 극한을 생각하면 이해가 쉬울지도?

* 최악의 상황을 고려

* 시스템에 대한 감을 익히기
  * python에서 대충
  * 1M / 1sec : 안정적
  * 10M ~ 50M / 1sec : 대다수 가능
  * 100M / 1sec : 거의 불가능


## 시간복잡도
![big O complexity chart](img/2022-07-22-22-58-58.png)

O(N!) > O(2$^N$) > O(N$^2$) > O(N$log{N}$) > O(N) > O($\sqrt{n}$) > O($log{N}$) > O(1)

### O(1) constant time
* 입력크기에 상관없이 언제나 일정한 시간이 걸리는 알고리즘
```python
# 1부터 N까지 합
def sum_num(N):
    return N * (N + 1) // 2
```
```python
def drop_constant(N):
    for i in range(N):
        print(i)
    for j in range(N):
        print(j)
```
### O(N) linear time
* n번 루프
```python
def point_1d(N):
    point = []
    for i in range(N):
        point.append(i)
    return point
```

### O(N$^{2}$) quadratic time
* n x n
```python
def point_2d(N):
    point = []
    for i in range(N):
        for j in range(N):
            point.append([i, j])
    return point
```

### O(NM) quadratic time
* n x m
```python
def point_2d(N, M):
    point = []
    for i in range(N):
        for j in range(M):
            point.append([i, j])
    return point
```

### O(N$^3$) cubic time / polynomial time
* n x n x n
```python
def point_3d(N):
    point = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                point.append([i, j, k])
    return point
```

### O(2$^N$) exponential time
* fibonacci
* 호출할 때마다 두배씩 증가
```python
def fibonacci(N):
    if N == 0 or N == 1:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)
```
### O(M$^N$) exponential time
* 호출할 때마다 M배씩 증가

### O($log{N}$)
* binary search 이분탐색
* 루프마다 1/2씩 감소
```python
def binary_search(str, end, key, lst):
    mid = int((str + end) / 2)
    if lst[mid] == key: return key
    elif lst[mid] > key: return binary_search(str, mid - 1, key, lst)
    else: return binary_search(mid + 1, end, key, lst)
```
### O($\sqrt{N}$)
* 루프N에 대해 sqrt(N)까지 진행

---

## sort 정렬
* python에서는 .sort() , sorted() 를 잘 사용하면 된다.
* key= lambda x:x[] 활용하기
* 예제 [단어 정렬 1181](https://www.acmicpc.net/problem/1181)
```python
lst = ['asdf', 'a', 'qwerty', 'bnm']
ret = sorted(lst, key= lambda x : len(x), reverse= False)
```

[sort algorithm](https://gyoogle.dev/blog/algorithm/Bubble%20Sort.html)

* 연습
![연습](img/2022-07-30-13-20-57.png)

### bubble sort 버블 정렬
1. 1회차 : 첫 번째, 두 번째 비교 / 두 번째, 세 번째 비교 / ... / n-1 번째, n 번째 비교
2. 1회차 결과 가장 큰 값이 맨뒤로
3. 2회차 : 1.반복 / ... / n-2 번째, n-1 번째 까지
4. 반복
```python
```
* O(N$^2$)
* stable

### selection sort 선택 정렬
1. 배열에서 최소값/최대값 찾기
2. 그 값을 맨앞/맨뒤와 교체
3. 맨 앞/뒤를 제외한 배열에서 1.반복
4. 반복
```python
```
* O(N$^2$)
* unstable

### insertion sort 삽입 정렬
1. 2번째 원소부터 그 앞까지의 원소와 크기 비교, 들어갈 위치에 삽입
```python
```

### merge sort 병합 정렬
1. 배열의 중간을 기준으로 반으로 분할 (분할)
2. 나눠진 배열에서 1.반복 , 배열의 크기가 0이나 1까지
3. 최소 단위로 나눠진 배열의 값을 비교, 정렬 후 배열로 병합 (정복 병합)
4. 다음 단위의 인접한 두 배열 끼리 3.반복 
5. 배열 비교방법 중 하나 투포인터
```python
```

* 평균 : O(N$log{N}$)
* stable

### quick sort 퀵 정렬
1. 배열에서 하나의 원소를 선택 (피봇)
2. 해당 원소를 기준으로 기준보다 작은 수는 앞으로, 큰 수는 뒤로 정렬
3. 기준원소 앞 배열, 뒤 배열에서 각각 1. 반복
```python
```
* 평균 : O(N$log{N}$)
* 최악 : O(N$^2$)
* unstable
* 최악을 피하기 위해서 피봇을 랜덤 혹은 중앙값

### 등등
### 정렬 알고리즘 비교
* runtime , time coplelxity
* stable, unstable
* 장단점
* 용도
---

## 수학
* 간단한 기초 수학으로 문제를 쉽게 풀어보자!

### n진법
* n진법 변환으로 거듭제곱의 연산을 간소화할 수 있다.

123 = 1 x 100 + 2 x 10 + 3 x 0

123 = (((0 x 10 + 1) x 10) + 2) x 10 + 3 

* 예제 [곱 1629](https://www.acmicpc.net/problem/1629)

* A^11 / 12

* A * A^2 * A^8
```python
def cal_power(a, b, c):
    ret = 1
    while b:
        if b % 2 == 1: ret *= a
        a = a * a
        b //= 2
    return ret % c

cal_power(10, 11, 12)
```
```python
# 큰 수끼리의 곱이 느려, 아래가 좀 더 빠름
def cal_power(a, b, c):
    ret = 1
    while b:
        if b % 2 == 1: ret = ret * a % c
        a = a * a % c
        b //= 2
    return ret

cal_power(10, 11, 12)
```

### LCM 최소공배수 , GCD 최대공약수
* 예제 [최대공약수와 최소공배수 2609](https://www.acmicpc.net/problem/2609)
* LCM 최소공배수
  * 공통적인 배수 중 최소값
  * LCM(a , b) = a x b / GCD(a , b)
  * GCD를 알면 O(1)으로 계산 가능

* GCD 최대공약수
  * 공통적인 약수 중 최대값이 1이면 서로소

```python
def gcd(a, b):
    ret = 0
    for i in range(min(a, b)):
        if a % i == 0 and b % i == 0:
            ret = i
    return ret
```
```python
# target의 위치를 예상하면 더 빠르게 짤 수 있다
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
```

* 유클리드 호제법
  * GCD(a , b) = GCD(b , a % b)

```python
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
```

### 소수 판별법
* 예제 [소수 찾기 1978](https://www.acmicpc.net/problem/1978)
* 소수 판별
```python
def isPrime(N):
    for i in range(2, N):
        if N % i == 0: return False
    return True
# O(N)

def isPrime(N):
    i = 2
    while i * i <= N:
        if N % i == 0: return False
        i += 1
    return True
# O(sqrt(N))
```
* sqrt(N)까지 검사

* 예제 [소수 구하기 1929](https://www.acmicpc.net/problem/1929)
* 에라토스테네스의 체
  * N까지의 소수를 구하려면 sqrt(N)까지의 소수의 배수를 제거
```python
def eratos(N):
    check, prime = [False for _ in range(N + 1)], []
    for i in range(2, N + 1):
        if check[i] == True: continue
        prime.append(i)
        for j in range(i * i, N + 1, i):
            check[j] = True
    return check, prime

print(eratos(50))
# Nlog(log(N))
```
### 재귀함수
* 예제 [하노이 탑 11729](https://www.acmicpc.net/problem/11729)
* 점화식
  * F(N) = 2 x F(N - 1) + 1 , F(1) = 1
```python
def era(N):
    check, prime = [False for _ in range(N + 1)], []
    for i in range(2, N + 1):
        if check[i] == True: continue
        prime.append(i)
        for j in range(i * i, N + 1, i):
            check[j] = True
    return check, prime

print(era(50))

def hanoi(st, ed, sz):
    if sz == 1: return print(st, ed)
    hanoi(st, 6-st-ed, sz-1)
    print(st, ed)
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
print(2**n-1)
hanoi(1, 3, n)
```



## 참고
* [Big O notation](https://www.youtube.com/watch?v=6Iq5iMCVsXA)
  
* [수학](https://www.youtube.com/watch?v=t_Ezo4NksZY&list=PL9mhQYIlKEhfg0aLdaO04wYUovLMXY4DU&index=4)
  
* [정렬 알고리즘](https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4)