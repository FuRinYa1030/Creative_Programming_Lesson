
#----include----
import numpy as np
#import cupy as np
import random
import os
import cv2
import sys

#----include function----
N = 1024 #array size
R_Num_D = 23 #rule decimal
count = 1024 #number of process
random_initial_mode = 3 #mode numer 

#set1 N:41 count:50 mode:0 R_Num_D:23
#set2 N:41 count:50 mode:0 R_Num_D:126
#set3 N:100 count:100 mode:1 R_Num_D:90
#set4 N:100 count:100 mode:1 R_Num_D:170
#set5 N:100 count:100 mode:2 R_Num_D:150
#set6 N:100 count:100 mode:2 R_Num_D:110

radius = 1 #neighborhood radius
neighborhood_toggle = 0 
#0 Von Neumann neighborhood
#1 Moore neighborhood


White_Color = [209,228,228] #RGB - 1
Black_Color = [50,50,50] #RGB - 0
mag = 1

#----initial value print and mass size calculate----
if neighborhood_toggle == 0:
    mass_size = radius ** 2 + (radius + 1) ** 2
    print(" Neighborhood:",end="Von Neumann neighborhood")
else:
    mass_size = (2 * radius + 1) ** 2
    print(" Neighborhood:",end="Moore neighborhood")

print(" r:",end=str(radius))
print(" range:",end=str(mass_size))

print("")
print("Rule-Range:0 ~ ",end=str(2 ** (2 ** mass_size)))
R_Num_D = input(' Rule-Number?: ')


print("Rule:",end=str(R_Num_D))
print(" Size:",end=str(N))
print(" Count:",end=str(count))
print(" Mode:",end=str(0))



#----Video setting----
width_v = N*mag
height_v = N*mag
fps = 5.0

filepath = 'task4.avi'
fmt = cv2.VideoWriter_fourcc(*'MJPG')
#fmt = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(filepath, fmt, fps, (width_v, height_v))


#----rule convert decimal→binary and zero endless----
D = np.zeros((N,N))
if R_Num_D != "0":
    R_Num_B = bin(int(R_Num_D))[2:]
else:
    R_Num_B = "0"

format_table1 = str('{0:0' + str(2 ** mass_size) + 'd}')
R_Num_B = format_table1.format(int(R_Num_B))

R_Num_B_List = np.zeros(2 ** mass_size)
R_Num_B_List = list(R_Num_B)
R_Num_B_List.reverse()


#----comparison table generate----
NB = np.zeros((2 ** mass_size,mass_size))
for i in range(0,2 ** mass_size):
    NB_tem = bin(i)[2:]
    format_table2 = str('{0:0' + str(mass_size) +'d}')
    NB_tem = format_table2.format(int(NB_tem))
    NB[i,:] = np.array(list(NB_tem))


#----comparison table print----
print("")
for i in range(2 ** mass_size):
    print(R_Num_B_List[i],end=":")
    print(NB[i,:])
print("")


#----Clear console----
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#----Find a place other than Meinong's Point.----
def position_serch(m,n,i,j):
    posi_x = j + n
    posi_y = i + m

    if 0 > posi_x:
        posi_x = posi_x + N
    elif N - 1 < posi_x:
        posi_x = posi_x - N

    if 0 > posi_y:
        posi_y = posi_y + N
    elif N - 1 < posi_y:
        posi_y = posi_y - N

    return posi_x,posi_y


#----initial array value generate----
if random_initial_mode == 0:
    for i in range(N):
        for j in range(N):
            D[i,j] = random.randint(0,1)

elif random_initial_mode == 1:
    #Sierpinski gasket/The center of the array is 1
    center = int(N / 2)
    if N % 2 == 0:
        D[0,center] = 1
    else:
        D[0,center + 1] = 1

elif random_initial_mode == 2:
    for i in range(N):
        D[i,N - i - 1] = 1

elif random_initial_mode == 3:
    center = int(N / 2)
    for i in range(N):
        D[:,center + 1] = 1


#----initial array value print----
'''
print("初期値↓")
for i in range(N):
    for j in range(N):
        if D[i,j] == 0:
            print("□",end="")
        else:
            print("■",end="")
    print("")
'''

#----pizture setting and backgraund color setting----
img = cv2.imread("seed.png")
img = cv2.resize(img,(N*mag,N*mag))

for i in range(N):
    for j in range(N):
        if D[i,j] == 0:
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,0] = Black_Color[2]
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,1] = Black_Color[1]
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,2] = Black_Color[0]
        else:
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,0] = White_Color[2]
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,1] = White_Color[1]
            img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,2] = White_Color[0]

writer.write(img)



cv2.imshow("Initial",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----Main processing----
for sss in range(count):

    Ds1 = np.zeros((N,N))

    for i in range(N):
        for j in range(N):

            Ds2 = np.zeros(mass_size)

            l = 0
            for m in range(-radius,radius + 1):
                
                #Von Neumann neighborhood
                if neighborhood_toggle == 0:
                    for n in range(abs(m) - radius,-abs(m) + radius + 1):
                        posi_x,posi_y = position_serch(m,n,i,j)
                        Ds2[l] = D[posi_y,posi_x]
                        l = l + 1

                #Moore neighborhood
                else:
                    for n in range(-radius,radius + 1):
                        posi_x,posi_y = position_serch(m,n,i,j)
                        Ds2[l] = D[posi_y,posi_x]
                        l = l + 1

            #----comparison table search----
            for k in range(2 ** mass_size):
                
                '''
                print("Ds2:",end="")
                print(Ds2[:],end="")
                print(" NB[k,:]:",end="")
                print(NB[k,:],end="")
                print(" Ans",end="")
                print(Ds2[:] == NB[k,:],end="")
                '''

                judge = Ds2[:] == NB[k,:]

                if judge.all():
                    Ds1[i,j] = R_Num_B_List[k]
                    break
            
    D = Ds1

    
    #clearConsole()

    '''
    for iii in range(N):
        for jjj in range(N):
            if D[iii,jjj] == 0:
                print("□",end="")
            else:
                print("■",end="")
        print("")
    print("")
    '''
    
    

    img = cv2.imread("seed.png")
    img = cv2.resize(img,(N*mag,N*mag))
    for i in range(N):
        for j in range(N):
            if D[i,j] == 0:
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,0] = Black_Color[2]
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,1] = Black_Color[1]
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,2] = Black_Color[0]
            else:
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,0] = White_Color[2]
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,1] = White_Color[1]
                img[i*mag:(i+1)*mag,j*mag:(j+1)*mag,2] = White_Color[0]


    writer.write(img)
    #cv2.imshow("Initial",img)

    print("\r{0}:Prosess".format(sss), end="")


    
print("")
print("Finish")
writer.release()

cv2.imshow("Initial",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




