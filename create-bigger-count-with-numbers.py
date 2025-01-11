
def num(a,b):
    if a+b>b+a :
        return -1
    elif b+a>a+b:
        return 1
    else:
        return 0
        
i=[9,1,2,50]
nstr=[]
for n in i:
    nstr.append(str(n))

n=len(nstr)
for j in range(len(i)):
    for x in range(0,n-j-1):
        if num(nstr[x] , nstr[x+1])>0 :
            nstr[x],nstr[x+1]=nstr[x+1],nstr[x]

result=''.join(nstr)
print(result)
