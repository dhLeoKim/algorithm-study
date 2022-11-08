def solution(participant, completion):
    P = len(participant)
    p_dict = dict(zip(participant, [0]*P))
    for i in range(P):
        p_dict[participant[i]] += 1
    
    C = len(completion)
    for i in range(C):
        p_dict[completion[i]] -= 1

    for key, val in p_dict.items():
        if val:
            return key

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# participant = ["mislav", "stanko", "mislav", "ana", "mislav"]
# completion = ["stanko", "ana", "mislav", "mislav"]

print(solution(participant, completion))