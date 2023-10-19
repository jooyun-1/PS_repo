import math
def solution(fees, records):
    answer = []
    cars = []
    for i in range(len(records)) :
        if records[i][11:] == 'IN' :
            if records[i][0] == '0' :
                in_hour = int(records[i][1])
            else :
                in_hour = int(records[i][:2])
            if records[i][3] == '0' :
                in_min = int(records[i][4])
            else :
                in_min = int(records[i][3:5])
            in_time = 60*in_hour + in_min
            car_num = records[i][6:10]
            flag = False
            out_flag = False

            for j in range(i+1,len(records)) :
                if records[i][6:11] == records[j][6:11] and records[j][11:] == 'OUT':
                    out_flag = True
                    if records[j][0] == '0' :
                        out_hour = int(records[j][1])
                    else :
                        out_hour = int(records[j][:2])
                    if records[j][3] == '0' :
                        out_min = int(records[j][4])
                    else :
                        out_min = int(records[j][3:5])
                    out_time = 60*out_hour + out_min
                           
                    for c in cars :
                        if c[0] == car_num :
                            c[1] += out_time - in_time
                            flag = True
                    if flag == False :
                        cars.append([car_num,out_time-in_time,fees[1]])
                    break
            if out_flag == False :
                out_time = 60*23 + 59
                for c in cars :
                    if c[0] == car_num :
                        c[1] += out_time - in_time
                        flag = True
                if flag == False :
                    cars.append([car_num,out_time-in_time,fees[1]])
    cars.sort()
    for c in cars :
        if c[1] >= fees[0] :
            c[2] += math.ceil((c[1]-fees[0])/fees[2])*fees[3]
        answer.append(c[2])

    return answer