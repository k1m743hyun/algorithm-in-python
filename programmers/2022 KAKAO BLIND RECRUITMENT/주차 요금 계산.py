import math
import datetime


def solution(fees, records):
    parking = {}
    results = {}
    for record in records:
        time, car_num, in_out = record.split(' ')

        if in_out == 'IN':
            parking[car_num] = datetime.datetime.strptime(time, "%H:%M")
        else:
            if results.get(car_num):
                results[car_num] += datetime.datetime.strptime(time, "%H:%M") - parking.pop(car_num)
            else:
                results[car_num] = datetime.datetime.strptime(time, "%H:%M") - parking.pop(car_num)

    for car_num in parking:
        if results.get(car_num):
            results[car_num] += datetime.datetime.strptime('23:59', "%H:%M") - parking[car_num]
        else:
            results[car_num] = datetime.datetime.strptime('23:59', "%H:%M") - parking[car_num]

    answer = []
    for car_num, time in sorted(results.items(), key=lambda x: x[0]):
        hour, minute, _ = map(int, str(time).split(':'))
        minute += hour * 60

        fee = fees[1]
        if minute > fees[0]:
            fee += math.ceil((minute - fees[0]) / fees[2]) * fees[3]

        answer.append(fee)
    return answer
