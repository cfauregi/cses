def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])

N = int_input()
bit = 2 
n=1
for i in range(N):
	n = (n*2)%(1e9+7) ## modulo pour limiter les overflow comme en C++
print(int(n))
