p = int(raw_input())
str2=""
while(p):
    t = p%10
    p/=10
    str2 = str("0" + str(bin(t)[2:])) + str2
count=0
var =0
for x in xrange(0,len(str2)+1):

    if (str2[x:x+1]==str(var)):
        count+=1
    else:
        print count,
        var = (var+1)%2
        count=1

#45268
#1 1 3 1 1 1 1 1 2 2 2 1 3
