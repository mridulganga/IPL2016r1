tmem = int(raw_input())
allsize = int(raw_input())
str2= raw_input()
rmem = int(raw_input())
sizermem = raw_input()

sizer= sizermem.split(" ")

if len(str2)>(tmem/allsize):
    exit(1)
cspace=""

count=0
var =0
flag=0
for x in xrange(0,len(str2)+1):

    if (str2[x:x+1]=="0"):
        count+=1
    else:
        if count!=0:
            cspace += str(count)
        var = (var+1)%2
        count=0

news=0

for s in sizer:
    news = news*10 + int(round((float(s)/allsize)+0.4))
cspace = sorted(cspace,reverse=True)

news = list(str(news))

sum1=0
sum2=0
for i in xrange(0,len(news)):
    sum1+=int(news[i])
for i in xrange(0,len(cspace)):
    sum2+=int(cspace[i])


if sum1>sum2:
    print "NO"
else:
    print "YES"

