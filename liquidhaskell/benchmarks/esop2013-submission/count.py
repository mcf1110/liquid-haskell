#!/usr/bin/python

# used by count.sh

import re
import sys
import string

fname = sys.argv[1]
str = (open(fname, 'r')).read()

#measures =   [(str[a.start():(3+string.find(str,"@-}", a.start()))]) for a in list(re.finditer('{-@ measure', str)) ]
other =   [(str[a.start():(3+string.find(str,"@-}", a.start()))]) for a in list(re.finditer('{-@ (type|measure|data|include|predicate)', str)) ]
tyspecs  =   [(str[a.start():(3+string.find(str,"@-}", a.start()))]) for a in list(re.finditer('{-@ (?!(type|measure|data|include|predicate))', str)) ]

#print measures
#print tyspecs
#print other
#print "Measures        :\t\t count = %d \t chars = %d \t lines = %d"  %(len(measures), sum(map(lambda x:len(x), measures)), sum(map(lambda x:(1+x.count('\n')), measures)))
print "Type specifications:\t\t count = %d \t lines = %d" %(len(tyspecs), sum(map(lambda x:(1+x.count('\n')), tyspecs)))
print "Other Annotations  :\t\t count = %d \t lines = %d" %(len(other), sum(map(lambda x:(1+x.count('\n')), other)))


ftyspec = open('_'.join(["tyspec", fname, ".txt"]), 'w')
fother = open('_'.join(["other", fname, ".txt"]), 'w')

#tmp.write("TYSPECS\n\n")
tyspecsJoined = '\n'.join(tyspecs)
ftyspec.write(tyspecsJoined)

#tmp.write("\n\nOTHER\n\n")
otherJoined = '\n'.join(other)
fother.write(otherJoined)


