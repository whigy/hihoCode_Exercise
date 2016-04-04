__author__ = 'whigy'
#partly refer to http://blog.csdn.net/zhouyelihua/article/details/47664907

def checkBeauty(caseLen, case):

    if int(caseLen) < 3:
        return 'NO'
    ch = []
    #represent by list
    for x in case:
        ch.append(x)
    #represent by [char, count]
    cur = 0
    count = [[ch[0],1]]
    for k in range(int(caseLen)-1):
        k = k+1
        if ch[k-1] == ch[k]:
            count[cur][1] = count[cur][1] + 1
        else:
            count.append([ch[k],1])
            cur = cur + 1
    #print count

    #simple check
    #for j in range(int(caseLen)-2):
    #    if ord(ch[j])+1 == ord(ch[j+1]) and ord(ch[j+1])+1 == ord(ch[j+2]):
    #        return  'YES'

    #complex check
    if len(count) < 3:
        return 'NO'
    for j in range(len(count)-2):
        if  (ord(count[j][0])+1 == ord(count[j+1][0]) and ord(count[j+1][0])+1 == ord(count[j+2][0])) and (count[j][1] ==count[j+2][1] and count[j][1] >= count[j+1][1]):

            return  'YES'
    return 'NO'

if __name__  ==  "__main__":
    while True:
        foo = []
        try:
            (caseNum) = (int(raw_input("Number of Cases:"))) #for x in raw_input().split())
            for i in range(caseNum):
                caseLen = raw_input('Lengh of %d Cases:' %(i+1))
                case = raw_input('Case %d:' %(i+1))
                foo.append(checkBeauty(caseLen, case))
            for i in range(caseNum):
                print foo[i]
            break
        except EOFError:
            break









