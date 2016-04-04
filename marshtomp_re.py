__author__ = 'whigy'
#using regular expression
import re

while True:
    try:
        inp = raw_input()
        rpl = re.compile('marshtomp', re.I)
        print str(rpl.sub('fjxmlhx', inp))
    except EOFError:
        break
