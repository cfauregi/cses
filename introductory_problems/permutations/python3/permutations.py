def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])

N = int_input()
if N==2 or N==3:
	print("NO SOLUTION")
elif N==4 :
	print("2 4 1 3")
else:
	if N&1==1:
		n=int(N/2)+1
	else :
		n=int(N/2)
	Temp = [0]*N
	j=0
	for i in range(1,N+1,2):
		Temp[j]=i
		if j+n<N:
			Temp[j+n]=i+1
		j+=1
	for i in Temp:
		print(i,end=" ")

