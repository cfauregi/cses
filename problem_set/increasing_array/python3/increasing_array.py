def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])

N = int_input()
Vector = int_input()


Move = 0
if N >1:
	i_min=Vector[0]
	for i in range(len(Vector)) :
		while(i_min>Vector[i]):
			coef = i_min-Vector[i]
			Move += coef
			Vector[i] += coef
			#print(coef)
			#coef = i_min//Vector[i]
			#if (coef!=1)and Move >1:
			#	Move+=Vector[i]*coef-Vector[i]
			#	Vector[i]=Vector[i]*coef
			#else :
			#	Vector[i]+=1
			#	Move+=1
		i_min=Vector[i]
print(Move)
#print(Vector)

