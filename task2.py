from asyncio.windows_events import NULL
import math
import random
import os

os.system('cls')

p = []
q = [0,0,0,0]
per = [0.0,0.0,0.0,0.0]
RankSelect = [4,4,4,4]

Max_Num = 1048576
bin_len = len(bin(Max_Num)[2:])
print(bin_len)



NoT = 0

#MutationProbability = random.randint(1,100)
MutationProbability = 80

#Initial Population
for i in range(4):
	x = random.randint(0,Max_Num - 1)

	#binary values encoding
	x_b = bin(x)[2:]
	p.append(x_b)

	print(int(x_b,2),end="")
	print(":",end="")
	print(x_b)



def EndCondition(f):
	for i in f:
		#Fitness function f(x) Decimal value
		if int(i,2) >= (Max_Num - 1):
			return i
	return NULL


#---binary data processing---
#---selection sort---???
'''
for i in range(0,3):
	for j in range(i + 1,4):
		if int(p[i],2) <= int(p[j],2):
			EmptyBox = p[i]
			p[i] = p[j]
			p[j] = EmptyBox
'''

#---0 stuffing---
print("")
for i in range(4):
	p[i] = '{0:020d}'.format(int(p[i]))
	print(p[i])


while True:
	solution = EndCondition(p)
	

	if solution == NULL:
		os.system('cls')
		print(p)
		NoT += 1

		#---Roulette Wheel Selection Sum---
		Fitness_Sum = 0
		for i in range(4):
			Fitness_Sum += int(p[i],2)

		#---%of total(range)---
		for i in range(4):
			per[i] = int(p[i],2) / Fitness_Sum
			if i > 0:
				per[i] = per[i] + per[i - 1]
		
		#---Rounded down fourth decimal place---
		for i in range(4):
			per[i] = math.floor(per[i] * 1000) / 1000
		
		
		print("")
		print("Trial:",end="")
		print(NoT,end="")
		print(" %of total:",end="")
		print(per)

		#---Rank select---
		for i in range(4):
			Rank = random.randrange(0,1000)
			Rank /= 1000
			for j in range(4):
				if Rank < per[j]:
					RankSelect[i] = j + 1
					print("Rank:",end="")
					print(Rank)
					break
		

		print(RankSelect)
		print("")

		#---Crossover----
		for i in range(0,3,2):
			CrossoverPoint = random.randint(20 - bin_len,19)

			
			print("CrossoverPoint:",end="")
			print(CrossoverPoint)
			

			P1 = p[RankSelect[i] - 1]
			P2 = p[RankSelect[i + 1] - 1]

			C1 = P1[:CrossoverPoint] + P2[CrossoverPoint:]
			C2 = P2[:CrossoverPoint] + P1[CrossoverPoint:]

			q[i] = C1
			q[i + 1] = C2
			
			'''
			print("P1:",end="")
			print(P1)
			print("P2:",end="")
			print(P2)
			print("C1:",end="")
			print(C1)
			print("C2:",end="")
			print(C2)
			'''

		

		for i in range(4):
			q_pro = list(q[i])

			Threshold = random.randint(0,100)

			'''
			print("")
			print("MutationProbability:",end="")
			print(MutationProbability)
			print("Threshold:",end="")
			print(Threshold)
			'''		

			if Threshold <= MutationProbability:
				rand_posi = random.randint(22 - bin_len,20)

				if bin_len >= 17 and rand_posi <= 14:
					rand_length = random.randint(1,6)
					
				else:
					rand_length = random.randint(1,21 - rand_posi)

				for j in range(rand_length):
					if q_pro[rand_posi - 1 + j] == "0":
						q_pro[rand_posi - 1 + j] = "1"

					else:
						q_pro[rand_posi - 1 + j] = "0"

			ss = ""
			for s in q_pro:
				ss += s
			q[i] = str(ss)


		print("")
		print(q)


		p = q
		print("-------------------------------------------------")

		

		#solution = "1111111100"
		#break

	else:
		print(p)
		break



print("")
print("Answer is ",end="")
print(int(solution,2),end="")
print("   Trials are ",end="")
print(NoT)

print("MutationProbability:",end="")
print(MutationProbability,end="")
print("%")
			
