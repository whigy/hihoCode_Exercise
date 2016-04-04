__author__ = 'whigy'
#using regular expression
#however, hihoCoder doesn't support = =

import re

while True:
    try:
        inp = raw_input()
        rpl = re.compile('marshtomp', re.I)
        print str(rpl.sub('fjxmlhx', inp))
    except EOFError:
        break
