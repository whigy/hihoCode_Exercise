__author__ = 'whigy'

if __name__  ==  "__main__":
    while True:
        try:
            (x,y,z) = (int(x) for x in raw_input("differences:").split())
            diff = [x,y,z]
            diff.sort()
            print diff
            colors = raw_input("Color List:")
            color = []
            red = 0
            blue = 0
            yellow = 0
            max = 0
            diff_c = [0,0,0]
            max_temp = 0
            for x in colors:
                if x=='R':
                    red = red +1
                elif x == 'B':
                    blue = blue +1
                elif x == 'Y':
                     yellow = yellow +1
                max_temp = max_temp +1
                diff_c = [abs(red - blue), abs(blue-yellow), abs(yellow-red)]
                diff_c.sort()
                #print diff_c
                if cmp(diff,diff_c)==0:
                    if max_temp > max:
                        max = max_temp
                    max_temp = 0
                    red = 0
                    blue = 0
                    yellow = 0
                if max_temp > max:
                    max = max_temp
            print max
            break
        except EOFError:
            break