def odd_even (N):
	if N%2 == 0:
		return N/2

	else :
		return N*3+1

N = input()
N=int(N)
print(N)
while(N!=1):
	N = int(odd_even(N))
	print(N,end=" ")
