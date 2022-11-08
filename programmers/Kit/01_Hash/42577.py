def solution(phone_book):
    phone_book.sort()
    # print(phone_book)

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"]	
phone_book = ["12","123","1235","567","88"]	
phone_book = ["1235","567","88","213", "13", "12", "1236", "1239"]	
phone_book = ["11","12","111"]
phone_book = ["934793", "34", "44", "9347"]
phone_book = ["12","213","2235","567","88"]	

print(solution(phone_book))




#####################################
# def solution(phone_book):
#     print(sorted(phone_book))
#     phone_number = [{} for _ in range(10)]
#     for phone in phone_book:
#         idx = int(phone[0])
#         if phone_number[idx].get(len(phone), 0):
#             phone_number[idx][len(phone)] += [phone]
#         else:
#             phone_number[idx][len(phone)] = [phone]

#     print(phone_number)

#     for phone_dict in phone_number:
#         if len(phone_dict) <= 1:
#             continue
        
#         keys = list(phone_dict.keys())
#         keys.sort()
#         l = len(keys)

#         for i in range(l):
#             for pre in phone_dict[keys[i]]:
#                 for j in range(i+1, l):
#                     for number in phone_dict[keys[j]]:
#                         if number.startswith(pre):
#                             return False

#     return True