# 1108 update

from bisect import bisect_left

def solution(info, query):

    def createKey(idx, key, i):
        if idx == 4:
            if applicant.get(key, 0):                   # key: query 경우의수, val: 점수 로 구성된 hash
                applicant[key].append(info[i][4])
            else:
                applicant[key] = [info[i][4]]

            return
        
        createKey(idx+1, key + info[i][idx], i)
        createKey(idx+1, key + '-', i)
    
    N = len(info)
    for i in range(N):
        info[i] = list(info[i].split())
        info[i][4] = int(info[i][4])

    info.sort(key=lambda x: x[4])                       # 점수를 기준으로 정렬 후 자료구조에 저장하여, 이진 탐색 사용할 수 있게

    applicant = {}
    for i in range(N):
        createKey(0, '', i)                             # 한 지원자가 검색될 수 있는 모든 query 경우의 수 찾기

    result = []
    for cond in query:
        A, B, C, DE = cond.split(' and ')
        D, E = DE.split(' ')
        key = A + B + C + D
        if applicant.get(key):                         
            val = applicant[key]
            result.append(len(val) - bisect_left(val, int(E)))
        else:                                            # 생성되지 않는 key도 고려하기
            result.append(0)
    
    return result


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	

print(solution(info, query))

# 한 지원자가 검색될 수 있는 query의 모든 경우의 수 만들기



################################
# def solution(info, query):
#     keys = ['cpp', 'java', 'python', 'backend', 'frontend', 'junior', 'senior', 'chicken', 'pizza']
#     values = [[] for _ in range(len(keys))]
#     applicant = dict(zip(keys, values))
#     score = [0]
#     N = len(info)
#     for i in range(N):
#         temp = list(info[i].split(' '))
#         for j in range(4):
#             applicant[temp[j]].append(i+1)
#         score.append(int(temp[4]))

#     result = []
#     for inquiry in query:
#         A, B, C, DE = inquiry.split(' and ')
#         D, E = DE.split(' ')

#         lst = []
#         for cond in [A, B, C, D]:
#             if cond == '-':
#                 continue
#             lst.append(set(applicant[cond]))

#         if lst:
#             inter = lst[0]
#             for i in range(1, len(lst)):
#                 inter = inter & lst[i]
#         else:
#             inter = list(range(1, N+1))
        
#         E = int(E)
#         cnt = 0
#         for i in inter:
#             if score[i] >= E:
#                 cnt += 1
        
#         result.append(cnt)

#     return result



###################################
# def solution(info, query):
#     keys = ['cpp', 'java', 'python', 'backend', 'frontend', 'junior', 'senior', 'chicken', 'pizza']
#     values = [[] for _ in range(len(keys))]
#     applicant = dict(zip(keys, values))
#     score = [0]
#     N = len(info)
#     for i in range(N):
#         temp = list(info[i].split(' '))
#         for j in range(4):
#             applicant[temp[j]].append(i+1)
#         score.append(int(temp[4]))

#     result = []
#     for inquiry in query:
#         A, B, C, DE = inquiry.split(' and ')
#         D, E = DE.split(' ')

#         lst = []
#         for cond in [A, B, C, D]:
#             if cond == '-':
#                 continue
#             lst.append(set(applicant[cond]))
        
#         if lst:
#             inter = lst[0]
#             for i in range(1, len(lst)):
#                 inter = inter & lst[i]

#             if E == '-':
#                 result.append(inter)
#             else:
#                 cnt = 0
#                 E = int(E)
#                 for i in inter:
#                     if score[i] >= E:
#                         cnt += 1
#                 result.append(cnt)
#         else:
#             cnt = 0
#             E = int(E)
#             for idx in range(1, N+1):
#                 if score[idx] >= E:
#                     cnt += 1
#             result.append(cnt)

#     return result