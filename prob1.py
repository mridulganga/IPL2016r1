a=["c","d","e","f","g","a","b","C"]
s=raw_input()
for i in xrange(7,-1,-1):
    for j in xrange(0,len(s)):
        if(str(a[i])==str(s[j:j+1])): print "*",
        else: print "0",
    print "\n"
