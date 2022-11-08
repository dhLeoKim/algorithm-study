from itertools import combinations

def solution(orders, course):
    result = []
    for i in course:
        course_list = {}
        for order in orders:
            if i > len(order):
                continue
            for cb in  combinations(order, i):
                temp = ''.join(sorted(cb))
                if course_list.get(temp, 0):
                    course_list[temp] += 1
                else:
                    course_list[temp] = 1
    
        # print(course_list)
        # print(max(course_list.items(), key= lambda x: x[1]))
        menu_list = sorted(course_list.items(), reverse=True, key= lambda x: x[1])
        # print(menu_list)
        max_val = 2
        for menu in menu_list:
            if menu[1] >= max_val:
                max_val = menu[1]
                result.append(menu[0])
            else:
                break
        # break
    return sorted(result)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
course = [2,3,5]	
orders = ["XYZ", "XWY", "WXA"]	
course = [2,3,4]	

print(solution(orders, course))