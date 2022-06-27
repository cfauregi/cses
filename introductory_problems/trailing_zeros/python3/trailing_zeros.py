def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
 
N = int_input()
j=5
n=0
i=1
while(i>0):
	i=int(N/j)
	n=int(n+i)
	j=int(j*5)
print(n)
