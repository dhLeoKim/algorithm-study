# # 방법 1
# while True:
#     try: print(input())
#     except EOFError: break

# 방법 2
import sys

for s in sys.stdin:
    print(s, end = '')