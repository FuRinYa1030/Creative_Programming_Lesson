from tkinter import N
import numpy as np
import random
import os
import cv2
import time



N = 100
R_Num_D = 110
count = 100
random_initial_mode = 2
#set1 N:41 count:50 mode:0 R_Num_D:23
#set2 N:41 count:50 mode:0 R_Num_D:126
#set3 N:100 count:100 mode:1 R_Num_D:90
#set4 N:100 count:100 mode:1 R_Num_D:170
#set5 N:100 count:100 mode:2 R_Num_D:150
#set6 N:100 count:100 mode:2 R_Num_D:110



White_Color = [255,255,255] #RGB - 1
Black_Color = [50,50,50] #RGB - 0
mag = 5



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



if random_initial_mode == 0:
    for i in range(N):
        D[i] = random.randint(0,1)
elif random_initial_mode == 1:
    #Sierpinski gasket /The center of the array is 1
    center = int(N / 2)
    if N % 2 == 0:
        D[center] = 1
    else:
        D[center + 1] = 1
    count = N
elif random_initial_mode == 2:
    D[N - 1] = 1



print("初期値↓")
print("   ",end="")
for i in range(N):
    if D[i] == 0:
        print("□",end="")
    else:
        print("■",end="")
print("")


img = cv2.imread("seed.png")
img = cv2.resize(img,(N*mag,N*mag))


for i in range(N):
    if D[i] == 0:
        img[0:mag,i*mag:(i+1)*mag,0] = Black_Color[2]
        img[0:mag,i*mag:(i+1)*mag,1] = Black_Color[1]
        img[0:mag,i*mag:(i+1)*mag,2] = Black_Color[0]
    else:
        img[0:mag,i*mag:(i+1)*mag,0] = White_Color[2]
        img[0:mag,i*mag:(i+1)*mag,1] = White_Color[1]
        img[0:mag,i*mag:(i+1)*mag,2] = White_Color[0]



cv2.imshow("Initial",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


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

    for i in range(N):
        if D[i] == 0:
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,0] = Black_Color[2]
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,1] = Black_Color[1]
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,2] = Black_Color[0]
        else:
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,0] = White_Color[2]
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,1] = White_Color[1]
            img[k*mag:(k+1)*mag,i*mag:(i+1)*mag,2] = White_Color[0]

    cv2.imshow("Initial",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

