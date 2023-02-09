import sys
pitch = sys.stdin.readline().split()
flag = ''
for i in range(0, len(pitch)) :
    if i == len(pitch) - 1 :
        break
    if flag != 'descending' and int(pitch[i]) < int(pitch[i+1]) :
        flag = 'ascending'
    elif flag != 'ascending' and int(pitch[i]) > int(pitch[i+1]) :
        flag = 'descending'
    else :
        flag = 'mixed'
        break
print(flag)