from PIL import Image
import numpy as NP
from matplotlib import pyplot as plt

i=Image.open('i5.jpg')

iar=NP.asarray(i)

#print iar
b= len(iar)
p=0
for ii in iar:
    for jj in ii:
        p+=1

#print p
'''a=[]
for j in iar:
    for k in j:
        a.append(k[0])
#print a
s=int(NP.sum(a)/len(a))'''

#print s
ar=[[[0 for _ in range(3)]for _ in range (int(p/b))] for _ in range(b)]
for ii in range(b):
    for jj in range (int(p/b)):
        ar[ii][jj][2]=0
        ar[ii][jj][1]=0
for ii in range(b):
    for jj in range (int(p/b)):
        ar[ii][jj][0]=iar[ii][jj][0]#-s
        '''if(ar[ii][jj][0]<0):
            ar[ii][jj][0]=int((ar[ii][jj][0]+s)*255/s)'''

#i.show()
plt.xticks([]),plt.yticks([])
plt.imshow(ar)
plt.show()

#print len(ar)