from audioop import reverse
from itertools import count
from posixpath import split
from re import A, S
from tkinter import N
import numpy as np
import random
import os

N = 41
R_Num_D = 5
count = 50

#90 85 170

D = np.zeros(N)





R_Num_B = bin(R_Num_D)[2:]
R_Num_B = '{0:08d}'.format(int(R_Num_B))

R_Num_B_List = np.zeros(8)
R_Num_B_List = list(R_Num_B)
R_Num_B_List.reverse()

NB = np.zeros((8,3))
for i in range(0,8):
    NB_tem = bin(i)[2:]
    NB_tem = '{0:03d}'.format(int(NB_tem))
    NB[i,:] = list(NB_tem)



print("Ruru:",end=str(R_Num_D))
print("")
for i in range(8):
    print(R_Num_B_List[i],end=":")
    print(NB[i,:])
print("")



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



print("初期値↓")
print("   ",end="")
for i in range(N):
    D[i] = random.randint(0,1)
    
    if D[i] == 0:
        print("□",end="")
    else:
        print("■",end="")
print("")



for k in range(count):

    Ds = np.zeros(N)

    for i in range(N):
        for j in range(8):
            if i > 0 and i < N - 1:
                a = i - 1
                c = i + 1

            elif i == 0:
                a = N - 1
                c = i + 1
                
            else:
                a = i - 1
                c = 0

            if D[a] == NB[j,0] and D[i] == NB[j,1] and D[c] == NB[j,2]:
                Ds[i] = R_Num_B_List[j]
                break
                
    D = Ds

    print('{0:02d}'.format(k+1),end="")
    print(":",end="")
    for s in range(N):
        if D[s] == 0:
            print("□",end="")
        else:
            print("■",end="")
    print("")




