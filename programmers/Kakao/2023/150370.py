def solution(today, terms, privacies):
    yyyy, mm, dd = map(int, today.split('.'))

    # 약관 종류 정리하기
    terms_dict = {}
    for _ in terms:
        type, period = _.split(' ')
        terms_dict[type] = int(period)

    # 유효기간 계산
    ret = []
    for i in range(len(privacies)):
        day, type = privacies[i].split(' ')
        y, m, d = map(int, day.split('.'))
        diff = (yyyy - y)*12*28 + (mm - m)*28 + (dd - d)    # day로 변환해서 유효기간 넘겼는지 확인

        if diff/28 >= terms_dict[type]:
            ret.append(i+1)

    return ret

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# [1, 3]

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# # [1, 4, 5]

print(solution(today, terms, privacies))