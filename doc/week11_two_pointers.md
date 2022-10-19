# week11 two pointers
1. two pointers
2. sliding window

## two pointers
* 이중 for문으로 O(N^2)에 처리되는 작업을
* 두 개의 포인터를 사용하여 O(N)에 처리하는 알고리즘
* 시작점 끝점 두개의 포인터로 데이터의 범위 표현

## 예제
* ex) 합이 M인 부분 연속 수열 : [1, 2, 3, 2, 5]
1. 시작점 start, 끝점 end 를 idx=0에서 시작
2. 현재 부분 합이 M과 같다면 cnt++
3. 현재 부분 합이 M보다 작다면, end++
4. 현재 부분 합이 M보다 크거나 같다면, start++
5. 리스트 끝까지 반복
```python
lst = [1, 2, 3, 2, 5]
M = 5

end = 0
interval = 0
cnt = 0

for start in range(len(lst)):
    while interval < M and end < len(lst):
        interval += lst[end]
        end += 1
    
    if interval == M:
        cnt += 1
    interval -= data[start]
```

### merge sort 병합 정렬
### quick sort 퀵 정렬
* [week1](./week1_sort.md)

### boj
* boj 2230 수 고르기
* https://www.acmicpc.net/problem/2230

* boj 1806 부분합
* https://www.acmicpc.net/problem/1806

## sliding window
* 배열의 부분 배열을 창문으로 보고 탐색을 진행하면서 주어진 작업을 O(N)에 처리하는 알고리즘
* 반복적으로 계산하지말고, 겹치는 구간 기준 앞 뒤를 계산하는 아이디어
* S[a:b+1] = S - A + B

## 예제
* [7, 2, 4, 1, 6, 5, 8, 3]
* ex) 길이가 M인 부분 수열의 합
```python
lst = [7, 2, 4, 1, 6, 5, 8, 3]
N = len(lst)

start = 0
end = 0
window = 0
while end < N:
    window += lst[end]
    end += 1

    while start < end and winow >= min_val:
        window -= - lst[start]
        start += 1
```

### boj
* boj 2559 수열
* https://www.acmicpc.net/problem/2559
* boj 11003 최솟값 찾기
* https://www.acmicpc.net/problem/11003

## 구간 합
* 특정 구간의 합을 계산
* ex) [10, 20, 30, 40, 50] 에서 idx 1 ~ 3 사이의 합?
* 접두사 합 prefix sum : 배열의 맨 앞부터 특정 위치까지의 합을 미리 준비
* 누적합 미리 구해두고 prefix_sum[3] - prefix_sum[1] 로 상수시간에 해결