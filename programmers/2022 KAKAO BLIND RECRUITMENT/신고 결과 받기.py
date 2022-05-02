def solution(id_list, report, k):
    report_dict = {}
    for data in report:
        if report_dict.get(data.split(' ')[-1]):
            report_dict[data.split(' ')[-1]].append(data.split(' ')[0])
        else:
            report_dict[data.split(' ')[-1]] = [data.split(' ')[0]]    
    
    answer = [0] * len(id_list)
    for idx, val in report_dict.items():
        if len(set(val)) >= k:
            for id in set(val):
                answer[id_list.index(id)] += 1
    
    return answer