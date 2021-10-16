a=int(input())
for i in range(a):
    b=int(input())
    c=input()
    d=[]
    f=[]
    if len(c)%4!=0:
        print("ERROR...!!")
    elif len(c)%4==0:
        for j in range(0,len(c)+1,4):
            d.append(j)
        for k in range(len(d)-1):
            e=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
            for l in range(d[k],d[k+1]):
                if c[l]==str(0):
                    del e[(len(e)//2):len(e)]
                elif c[l]==str(1):
                    del e[0:(len(e)//2)]
            f.append(e[0])
    g=''.join([m for m in f])
    print(g)
