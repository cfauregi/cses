def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
import math
#N = int_input()
file = open("test_input.txt","r")
N = file.read()
file.close()
N = N.split("\n")
#print(N)
#print(N[0])
N = N[1:-1:]
n = [i.split(' ') for i in N]
#print(n)
#for i in range(0,len(N),2):
for i in n: 
#	n = int_input()
	print(1)
	#print(math.pow(int(i[0]),int(i[1]))%(10**9+7))
