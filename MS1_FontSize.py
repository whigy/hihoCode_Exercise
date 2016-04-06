__author__ = 'whigy'

import math

def calsizie(N, P, W, H, A):
    S = 1.0

    while True:
        height = 0
        if S > min(W,H):
            return S-1
        hei_page = math.floor(H/S)  #given size S, how many lines can be displyed in a page
        wid_page = math.floor(W/S)  #given size S, how many characters can be displyed in a line
        for i in range(N):
            row =  math.ceil(A[i]/wid_page)
            height  = height + row
        maxpage = math.ceil(height/hei_page)
        if maxpage <= P:
            S = S+1
            continue
        else:
            return S-1

if __name__  ==  "__main__":
    while True:
        try:
            T = int(raw_input())

            A = []
            for i in range(T):
                [N, P, W, H] = [int(x) for x in raw_input().split()]
                A = [float(x) for x in raw_input().split()]
                #print [N, P, W, H]#
                #print A#
                print int(calsizie(N, P, float(W), float(H), A))
            break
        except EOFError:
            break