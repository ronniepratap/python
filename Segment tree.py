fenar=[0 for x in range(400004)]
def construct(ar,val,l,r):
    if(l==r):
        fenar[val]=ar[l]
        return
    m=l+(r-l)//2
    construct(ar, 2*val+1, l, m)
    construct(ar, 2*val+2, m+1, r)
    fenar[val]= fenar[2*val+1] +fenar[2*val+2]

def query(l,r,s,e,val):
    if(r<s or l>e):
        return 0
    elif(l<=s and r>=e):
        return fenar[val]
    m= s +(e-s)//2
    ans=query(l, r, s, m, 2*val+1)+query(l, r, m+1, e, 2*val+2)
    return ans
def updatefen(l,r,ind,x,val):
    if l==r:
        fenar[ind]==x
        return
    m=l+(r-l)//2
    if(l<=ind and ind<=m):
        updatefen(l, m, ind, x, 2*val+1) 
    else:             
        updatefen(m+1, r, ind, x, 2*val+2)  
    fenar[val]= fenar[2*val+1] +fenar[2*val+2]    
                

n=int(input())              
ar=[0 for x in range(n)]
for x in range(n):
    v=int(input())
    count=0
    while(v):
        if(v & 1):
            count+=1
        v=v//2    
    if(count & 1):
        ar[x]=1
construct(ar, 0, 0, n-1)
q,qin=map(int,input().split())
while(q):
    q-=1
    qt,l,r,k=map(int,input().split())
    l-=1
    if(qt==2):
        updatefen(0, n-1, l, r, 0)
        continue
    r-=1
    sol=query(l, r, 0, n-1, 0)
    if(sol<k):
        print("No")
    else:
        sol-=k
        if(sol&1):
            print("No")
        else:
            print("Yes")    
                
