def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])

N = int_input()
Vector = []
Compare_vector = []
Vector = int_input()
for i in range(1,N):
	Compare_vector.append(i)
Compare_vector.append(N)
if type(Vector)!=int:
	print(sum(Compare_vector)-sum(Vector))
else :
	print(sum(Compare_vector)-Vector)

