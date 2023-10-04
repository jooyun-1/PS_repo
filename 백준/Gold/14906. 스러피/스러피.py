import sys
N = int(sys.stdin.readline())
print("SLURPYS OUTPUT")

def checkSlump(s) :
    global flag2
    # print("slump",s)
    if s[0] == 'D' or s[0] == 'E' :
        index = 1
        if len(s) >= 2 :
            while True :
                if s[index] != 'F' :
                    break
                index += 1
                if len(s) <= index :
                    index -= 1
                    break
            # print("index",s,s[index],index)
            # print("center",s)
            if s[index:] == 'G' :
                s = s[-1]
            else :
                s = s[index:]
                # print(s)
            # print("final",s)
            if s == 'G' :
                # print("t")
                flag2 = True
                # print("flag2",flag2)

            elif s[0] == 'D' or s[0] == 'E' :
                # print(s)
                checkSlump(s)
            else :
                flag2 = False
    else :
        flag2 = False
    # return False

def checkSlimp(s) :
    global flag1
    # print("sl",s)
    if len(s) >= 2 :
        if s[0] == 'A' :
            if len(s) == 2 :
                if s[1] == 'H' :
                    flag1 = True
                    return
                else :
                    flag1 = False
            elif len(s) >= 3 :
                # print("test2",s)
                if s[1] == 'B' :
                    checkSlimp(s[2:-1])
                    if s[0] == 'C' :
                        flag1 = True
                        return
                else :
                    # print("slump",s)
                    if len(s[1:]) == 3 :
                        checkSlump(s[1:])
                    else :
                        checkSlump(s[1:-1])
                    if flag2 == True and s[-1] == 'C' :
                        flag1 = True
                        return
        else :
            flag1 = False

for n in range(N) :
    s = sys.stdin.readline().rstrip()
    flag1, flag2 = False, False
    if len(s) < 2 :
        print("NO")
    else :
        for i in range(2,len(s)+1) :
            flag1, flag2 = False, False
            checkSlimp(s[:i])

            if flag1 == True :
                if i < len(s) :
                    if len(s) >= 2 :
                        temp = s
                        s = s[i:]
                        # print("test",s,flag2)
                        # if len(s) > 0 :
                        #     checkSlump(s)
                        if flag1 == True and flag2 == True :
                            # print(s)
                            if len(s) > 0 :
                                checkSlump(s)
                            if flag2 == True :
                                print("YES")
                                break
                        checkSlump(s)
                        # print(n,s,flag1,flag2)
                        if flag2 == True :
                            print("YES")
                            break
                        s = temp

                        # print(s)
                        # else :
                        #     print("NO")
                        #     break
            flag1 = False
        #     print("2",flag1,s)
        # print(flag1,s)
        if flag1 == False:
            # print(flag1,flag2)
            print("NO")

print("END OF OUTPUT")