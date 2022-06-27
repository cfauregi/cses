def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
 
N = int_input()

for i in range(1,N+1):
    temp = int((i-1)*(i+4)*((i**2)-(3*i)+4)/2) ## p.283 non attacking chess pieces Václav Kotěšovec             
    print(temp)
