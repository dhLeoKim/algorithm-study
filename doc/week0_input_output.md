# week1 : I/O
## input

## output
* list 출력 방법
  * *lst
  * '\n'.join(map(str, lst))
```python
lst = [1, 5, 2, 8, 3]

print(*lst)
# 1 5 2 8 3

print('\n'.join(map(str, lst)))
# 1
# 5
# 2
# 8
# 3
```