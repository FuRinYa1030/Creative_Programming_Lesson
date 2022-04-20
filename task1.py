from asyncio.windows_events import NULL
import math
import random

p = []
per = [0.0,0.0,0.0,0.0]
RankSelect = [4,4]

#Initial Population
for i in range(4):
	x = random.randint(0,31)

	#binary values encoding
	x_b = bin(x)[2:]
	p.append(x_b)

	print(int(x_b,2),end="")
	print(":",end="")
	print(x_b)



def EndCondition(f):
	for i in f:
		#Fitness function f(x) Decimal value
		if int(i,2) >= 31:
			return i
	return NULL



while True:
	solution = EndCondition(p)
	if solution == NULL:
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
			p[i] = '{0:05d}'.format(int(p[i]))
			print(p[i])

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
		print("%of total:",end="")
		print(per)

		#---Rank select---
		Rank1 = random.randrange(0,1000)
		Rank1 /= 1000
		for i in range(4):
			if Rank1 < per[i]:
				RankSelect[0] = i + 1
				print("Rank1:",end="")
				print(Rank1)
				break
		
		while True:
			toggle = False
			Rank2 = random.randrange(0,1000)
			Rank2 /= 1000

			for i in range(4):
				if Rank2 < per[i] and RankSelect[0] != i + 1:
					RankSelect[1] = i + 1
					toggle = True
					break

			if toggle == True:
				print("Rank2:",end="")
				print(Rank2)
				break

		print(RankSelect)

		#---Crossover----
		
		CrossoverPoint = random.randint(1,5)

		print("")
		print("CrossoverPoint:",end="")
		print(CrossoverPoint)

		P1 = p[RankSelect[0] - 1]
		P2 = p[RankSelect[1] - 1]

		C1 = P1[:CrossoverPoint] + P2[CrossoverPoint:]
		C2 = P2[:CrossoverPoint] + P1[CrossoverPoint:]
		
		print("P1:",end="")
		print(P1)
		print("P2:",end="")
		print(P2)
		print("C1:",end="")
		print(C1)
		print("C2:",end="")
		print(C2)
	

		solution = 0b11100
		break

		


		


	else:
		break
print("")
print("Answer is ",end="")
print(solution)
			
