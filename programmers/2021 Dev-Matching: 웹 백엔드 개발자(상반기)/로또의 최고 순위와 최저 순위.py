def solution(lottos, win_nums):    
    match_cnt = 0
    zero_cnt =  0
    for lotto in lottos:
        if lotto:
            if lotto in win_nums:
                match_cnt += 1
        else:
            zero_cnt += 1
    
    return [6 if match_cnt + zero_cnt < 1 else 7 - (match_cnt + zero_cnt), 6 if match_cnt < 1 else 7 - match_cnt]