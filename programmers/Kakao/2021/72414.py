from heapq import heappush, heappop
from collections import deque

def solution(play_time, adv_time, logs):
    # logs_int = []
    # for log in logs:
    #     st, ed = log.split('-')
    #     logs_int.append([int(''.join(st.split(':'))), int(''.join(ed.split(':')))])

    # logs_int.sort()
    # print(logs_int)



    def calAdv(st, adv_time):
        st_h, st_m, st_s = st.split(':')
        ad_h, ad_m, ad_s = adv_time.split(':')

        ed_h, ed_m, ed_s = 0, 0, 0
        ed_s = int(st_s) + int(ad_s)
        if ed_s >= 60:
            ed_m += 1
            ed_s = ed_s - 60
        ed_s = '0'*(2-len(str(ed_s))) + str(ed_s)

        ed_m += int(st_m) + int(ad_m)
        if ed_m >= 60:
            ed_h += 1
            ed_m = ed_m - 60
        ed_m = '0'*(2-len(str(ed_m))) + str(ed_m)

        ed_h = str(ed_h + int(st_h) + int(ad_h))
        if len(ed_h) > 2:
            return '99:59:59'
        else:
            ed_h = '0'*(2-len(ed_h)) + ed_h

        return str(ed_h) + ':' + str(ed_m) + ':' + str(ed_s)

    N = len(logs)
    logs_lst = []
    for log in logs:
        st, ed = log.split('-')
        logs_lst.append([st, ed])

    # logs_deque = deque(sorted(logs_lst))
    # print(logs_deque)
    logs_lst.sort()
    print(logs_lst)
    
    max_v = 0
    adv = []
    for i in range(N):
        # st, ed = log.split('-')
    
        print()
        num = 1
        adv_ed = calAdv(logs_lst[i][0], adv_time)
        if adv_ed > play_time:
            adv_ed = play_time
        
        if logs_lst[i][1] <= adv_ed:
            # 광고시간 보다 짧을 때
            # result = i번째 구간 길이
            pass
        else:
            # 광고시간 보다 길 때
            # result = 광고 끝 - i번째 시작
            pass
        
        print(logs_lst[i][0], adv_ed)

        for nxt in range(i+1, N):
            if logs_lst[nxt][0] > adv_ed:
                break
            print('st', logs_lst[nxt][0])
            num += 1
        
        for pre in range(i-1, -1, -1):
            # print('ed', logs_lst[pre][1])
            if logs_lst[pre][1] <= logs_lst[i][0]:
                break
            num += 1
        
        print(num)
        if num > max_v:
            max_v = num
            adv = [[logs_lst[i][0], adv_ed]]
        elif num == max_v:
            adv.append([logs_lst[i][0], adv_ed])

    print(max_v, adv)

    # 1. 중복되는 구간 개수의 최대값 구하기
    # 2. 최대 구간의 광고 재생 시간 구하기
    # 3. 재생시간이 긴 것 선택
    # 4. 재생시간이 같다면 빠른 시작 시간 선택
    # +) 문자열 시간 처리, 뺄셈 처리
    
    return 

play_time = "02:03:55"	
adv_time = "00:14:15"	
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# play_time = "99:59:59"	
# adv_time = "25:00:00"	
# logs = 	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# play_time = "50:00:00"	
# adv_time = "50:00:00"	
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))

print('00:41:59' >= '00:41:59')