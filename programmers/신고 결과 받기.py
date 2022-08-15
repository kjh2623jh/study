# def solution(id_list, report, k):
#     report = set(report)
#     mail = [0]*len(id_list)
#     report_cnt = [0]*len(id_list)
#     report_list = [x.split() for x in report]
    
#     for i in report_list:
#         report_cnt[id_list.index(i[1])] += 1
    
#     for i in range(len(id_list)):
#         if report_cnt[i] >= k:
#             for j in [x[0] for x in report_list if x[1] == id_list[i]]:
#                 mail[id_list.index(j)] += 1

#     return mail
#     # 테스트3: 타임아웃

# def solution(id_list, report, k):
#     report = [x.split() for x in set(report)]
#     report_list = {}

#     for i in id_list:
#         report_list[i] = [0]
#     for i in report:
#         report_list[i[1]].append(i[0])
#     for i in id_list:
#         if len(report_list[i]) > k:
#             for j in report_list[i]:
#                 if j == 0: continue
#                 report_list[j][0] += 1

#     return [x[0] for x in report_list.values()]
#   딕셔너리로 만들어보려했지만 더 난잡해짐.

def solution(id_list, report, k):
    report = set(report)
    mail = [0]*len(id_list)
    report_cnt = [0]*len(id_list)
    report_list = [x.split() for x in report]
    udict = {}

    for i,j in enumerate(id_list):
        udict[j]=i
    
    for i in report_list:
        report_cnt[udict[i[1]]] += 1
    
    for i in range(len(id_list)):
        if report_cnt[i] >= k:
            for j in [x[0] for x in report_list if x[1] == id_list[i]]:
                mail[udict[j]] += 1

    return mail


if __name__ == "__main__":
    print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
    ))
    #result: [2,1,1,0]

    print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
    ))
    #result: [0,0]


# 100점