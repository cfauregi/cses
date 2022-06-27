def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
 
N = int_input()
for i in range(N):
    n = int_input()
    if (n[0]<n[1]):
        big = n[1]
        small = n[0]
    else :
        small = n[1]
        big = n[0]
    if ((((big+small)%3==0) and (big!=0) and (small!=0) and (small>=int(big/2))) or ((big==0) and (small==0))):
        print("YES")
    else :
        print("NO")
