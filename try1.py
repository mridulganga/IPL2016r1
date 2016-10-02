a=raw_input()

count=[]
for j in range(0,len(a)):

    for i in range(j,len(a)):
        if (a[j:i+1]==a[i:j-1:-1]):

            count.append(i+1-j)

print max(count)
