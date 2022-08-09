import sys

def check_VPS(lst):
    vps = []
    for i in lst:
        if i == "(":
            vps.append(i)
        elif i == ")":
                if len(vps):
                    vps.pop()
                else:
                    vps.append(i)
                    break

    return "NO" if len(vps) else "YES"

T = int(input())

for i in range(T):
    lst = sys.stdin.readline().strip()
    print(check_VPS(lst))