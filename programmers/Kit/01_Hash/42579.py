def solution(genres, plays):
    table = {}
    for i in range(len(genres)):
        if table.get(genres[i], 0):
            table[genres[i]][0].append((plays[i], i))
            table[genres[i]][1] += plays[i]
        else:
            table[genres[i]] = [[(plays[i], i)], plays[i]]
    
    table_val = list(table.values())
    table_val.sort(reverse=True, key= lambda x: x[1])

    ret = []
    for temp in table_val:
        music = temp[0]
        music.sort(reverse=True, key= lambda x: x[0])
        for i in range(len(music)):
            if i == 2:
                break
            ret.append(music[i][1])

    return ret

genres = ["classic", "pop", "classic", "classic", "pop", "rock", "rock"]	
plays = [500, 600, 150, 800, 2500, 8000, 8000]	
print(solution(genres, plays))













#############################################
# def solution(genres, plays):
#     g = {}
#     p = {}
#     for i in range(len(genres)):
#         if g.get(genres[i], 0):
#             g[genres[i]][0] += plays[i]
#             g[genres[i]][1].append([plays[i], i])
#         else:
#             g[genres[i]] = [plays[i], [[plays[i], i]]]

#     # print(g)

#     play = list(g.values())
#     # print(play)
#     play.sort(reverse=True, key= lambda x: x[1][0])
#     # print(play)

#     album = []
#     for genre in play:
#         print(genre[1])
#         genre[1].sort(key= lambda x: x[1])
#         genre[1].sort(reverse=True)
#         print('aa', genre[1])
#         for i in range(len(genre[1])):
#             if i == 2:
#                 break
#             album.append(genre[1][i][1])

#     return album