def tt (n):
    return int(n*(n+1)) / int(2)
    
def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
import time 
N = int_input()
t = tt(N)
temps = time.time()
if t%2==0:
    print("YES")
    pack1= []
    sum_pack1=0
    sum_pack2=0
    pack2= []
    o=N
    for i in range(1,N+1):
        if sum_pack1<=sum_pack2:
        #if sum(pack1)<=sum(pack2):
        #Si on fait sa donne un temps de latence extremement grand
        # et ne respecte plus les critère donné par le problème                       
            pack1.append(o)
            sum_pack1+=o
        else :
            pack2.append(o)
            sum_pack2+=o
        #if i%10000==0:
        #        print('working               :',i)
        #        print('temps depuis le debut :', t-time.time())
        o=o-1
    print(len(pack1))
    for i in pack1:
            print(i,end=" ")
    print()
    print(len(pack2))
    for i in pack2:
            print(i,end=" ")
else : 
    print("NO")
