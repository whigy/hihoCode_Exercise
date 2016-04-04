__author__ = 'whigy'
while True:
    try:
        inp = raw_input()
        len_old = len('marshtomp')
        len_new = len('fjxmlhx')
        temp = inp.lower()
        inp = list(inp)
        while temp.rfind('marshtomp') != -1:
            idx = temp.rfind('marshtomp')
            inp[idx:(idx+len_old)] = []
            inp[idx:idx] = list('fjxmlhx')
            temp = temp[:idx]

        print ''.join(inp)
    except EOFError:
        break
