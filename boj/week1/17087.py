# 최대공약수 구하기
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, S = map(int, input().split())
brother = list(map(int, input().split()))

# 수빈과 동생사이의 거리값 D들의 최대공약수를 구해라
# D 값들 구하기
D_lst = []
for i in range(N):
    D_lst.append(abs(S - brother[i]))

# 여러 수의 최대공약수 구하는 방법
# 두 개씩 뽑아서 최대공약수 반복, 마지막에 남는 수 반환
D_gcd = D_lst[0]
for i in D_lst:
    D_gcd = gcd(i, D_gcd)

print(D_gcd)